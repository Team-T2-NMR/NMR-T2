# Author: Tyler Lazar
# Date: 2015-11-21

import urllib2, time
from BeautifulSoup import BeautifulStoneSoup

VALID_SOLVENT = 'Water'
MAX_PH = 7.5
MIN_PH = 6.5

INCHI_RESOLVER_URL = "http://cactus.nci.nih.gov/chemical/structure/{0}/stdinchi"
TIME_BETWEEN_URL_REQUESTS = 0.5

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
   
    # Get the inchi code
    try:
      info['inchi-code'] = \
          urllib2.urlopen(INCHI_RESOLVER_URL.format(info['inchi-key'])).read()
      time.sleep(TIME_BETWEEN_URL_REQUESTS)
      return info
    except: # Any exception, don't care which
      return None
  else:
    return None
