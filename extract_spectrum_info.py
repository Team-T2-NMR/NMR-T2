# Author: Tyler Lazar
# Date: 2015-11-21

from BeautifulSoup import BeautifulStoneSoup

VALID_SOLVENT = 'Water'
MAX_PH = 7.5
MIN_PH = 6.5

def extract_spectrum_info(filename):

  # Open the file
  with open(filename, 'r') as f:
    xml = f.read()
  
  # Extract the info
  soup = BeautifulStoneSoup(xml)
  info =   {'id': soup.find('id').contents[0],
            'database-id': soup.find('database-id').contents[0],
            'inchi-key': soup.find('inchi-key').contents[0],
            'solvent': soup.find('solvent').contents[0],
            'sample-ph': soup.find('sample-ph').contents[0],
            'frequency': soup.find('frequency').contents[0]}

  # Enforce spectrum validity rules
  if (  info['solvent'] == VALID_SOLVENT and
        float(info['sample-ph']) <= MAX_PH and
        float(info['sample-ph']) >= MIN_PH):
    return info
  else:
    return None
