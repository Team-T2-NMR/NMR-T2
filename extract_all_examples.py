# Author: Tyler Lazar
# Date: 2015-11-21

import glob
from extract_spectrum_info import *
from extract_examples_from_file import *

HMDB_SPECTRA_XML_LOCATION = './External' # Change this as needed
HMDB_SPECTRA_PEAK_LISTS_LOCATION = './External' # This too

ID_HEADER = 'Spectrum ID'
DATABASE_ID_HEADER = 'Database ID'
INCHI_KEY_HEADER = 'InChi Key'
SOLVENT_HEADER = 'Solvent'
SAMPLE_PH_HEADER = 'Sample pH'
FREQUENCY_HEADER = 'Frequency'
ATOM_HEADER = 'Atom number (pretend it\'s the corresponding InChI number for now)'
SHIFT_HEADER = 'Shift (ppm)'

def main():

  filenames = glob.glob(HMDB_SPECTRA_XML_LOCATION+"/hmdb_spectra_xml/HMDB*nmr_one_d*.xml")

  extracted_examples = []

  for filename in filenames:

    # Get the basic molecule and spectrum info
    spectrum_info = extract_spectrum_info(filename)

    # Skip this one if the spectrum info is invalid
    if (spectrum_info == None):
      continue

    # Get the corresponding peak file
    filename_rev = filename[::-1]
    spectrum_id = filename_rev[4:filename_rev.index('_')][::-1]
    peaklist_filenames = \
        glob.glob(HMDB_SPECTRA_PEAK_LISTS_LOCATION+"/hmdb_nmr_peak_lists/HMDB*oned*_{0}_*.txt".format(spectrum_id))

    # No corresponding peak file found for the xml
    if (len(peaklist_filenames) != 1):
      continue

    # Add the shift information to the example
    else:
      preprocessed_examples = extract_examples_from_file(peaklist_filenames[0])
      for preprocessed_example in preprocessed_examples:
        example = preprocessed_example.copy()
        for field, value in spectrum_info.iteritems():
          example[field] = value
        extracted_examples.append(example)

  return extracted_examples


if __name__ == '__main__':

  # Extract the data
  extracted_examples = main()

  # Print the extracted data as a tab-delimited table
  print '\t'.join([ ID_HEADER,
                    DATABASE_ID_HEADER,
                    INCHI_KEY_HEADER,
                    SOLVENT_HEADER,
                    SAMPLE_PH_HEADER,
                    FREQUENCY_HEADER,
                    ATOM_HEADER,
                    SHIFT_HEADER])
  for row in extracted_examples:
    print '\t'.join( [row['id'],
                      row['database-id'],
                      row['inchi-key'], 
                      row['solvent'], 
                      row['sample-ph'],
                      row['frequency'],
                      str(row['atom']),
                      str(row['shift'])])
