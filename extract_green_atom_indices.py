import os
import os.path
import re

def extract_nmr_atom_indices(peakfile_path, hmdb_id, output_folder):
	"""
	example: Process('./peakfiles/HMDB00001_nmroned_1022_27891.txt', 'HMDB00001', './output/')
	"""
	peak = open(peakfile_path, 'r')
	peak_buf = peak.read()
	peak.close()
	lines = peak_buf.split('\n')

	# regex for "table/list of assignments" header
	pat = re.compile('.*((able)|(ist)) [op]f ([Aa][sS]s).*')
	# make sure the header exists and there's only one
	assert any(pat.match(line) is not None for line in lines)
	assert len([1 for line in lines if pat.match(line) is not None]) == 1

	# index of line with "table of assignments"
	heading_index = None
	for index, line in enumerate(lines):
		if pat.match(line):
			heading_index = index

	# index of line with column headers (should be the line right after "table of assignments")
	labels_index = None
	for i in range(6):
		if lines[heading_index + 1 + i] != '':
			labels_index = heading_index + 1 + i
			break
	# make sure it's the right column headers (should be table of assignments and not table of multiplets)
	assert ('tom' in lines[labels_index] and 'ultiplet' in lines[labels_index] and 'tom1' not in lines[labels_index])

	# read the rows underneath the column headers
	text_start = labels_index + 1
	currentNo = 0
	atoms = []
	for index, line in enumerate(lines):
		if index < text_start:
			continue
		if line.strip() == '':
			break
		eles = line.split()
		no = int(eles[0])
		assert no == currentNo + 1
		currentNo = no
		atoms.append(eles[1] + '-')

	# get a list of sorted, unique atoms
	atoms = sorted(list(set(atoms)), key = lambda x: int(re.sub("\D", "", x)))

	output = '\n'.join(atoms)
	outf = open(output_folder + hmdb_id + '.txt', 'w')
	outf.write(output)
	outf.close()
