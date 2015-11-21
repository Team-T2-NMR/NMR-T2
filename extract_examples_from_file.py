# Author: Tyler Lazar
# Date: 2015-11-21

import sys

TABLE_NAME = 'Table of Assignments\n'
ATOM_LABEL = 'Atom '
ATOM_LABEL_INDEX = 1
SHIFT_LABEL = 'Exp. Shift (ppm) '
SHIFT_LABEL_INDEX = 2
NUM_LABELS = 4


def extract_examples_from_file(filename):

  extracted_examples = []

  table_reached = False
  table_labels_reached = False
  table_index = None

  with open(filename, 'r') as f:

    lines = f.readlines()

  for line in lines:

    if (table_index != None):
      table_index += 1


    if table_reached == True and table_labels_reached == True:

      entry = line.split('\t')

      # Make sure the entry has the expected number of fields
      if (len(entry) == NUM_LABELS):

        try:
          extracted_examples.append({'atom': int(entry[1]), 'shift': float(entry[2])})
        except ValueError:
          error_msg = 'The data at row {0} of the Table of Assignments was invalid' + \
                      '\n\t in file {1}'
          print >> sys.stderr, error_msg.format(table_index, filename)

      continue


    if table_reached == True and table_labels_reached == False:

      labels = line.split('\t')

      # Make sure all the expected columns are present and in the right order
      # (This constraint can be relaxed)
      if (len(labels) == NUM_LABELS and 
          labels[ATOM_LABEL_INDEX] == ATOM_LABEL and 
          labels[SHIFT_LABEL_INDEX] == SHIFT_LABEL):

        table_labels_reached = True

      continue


    if table_reached == False:
      if line == TABLE_NAME:
        table_reached = True
        table_index = 0
      continue

  return extracted_examples


if __name__ == '__main__':

  # Small test
  for row in extract_examples_from_file('External/hmdb_nmr_peak_lists/HMDB00001_nmroned_1022_27891.txt'):
    print 'Atom: '+str(row['atom'])+'; Shift: '+str(row['shift'])
