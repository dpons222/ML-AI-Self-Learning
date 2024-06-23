'''
The program will prompt for a URL, read the XML data from that URL 
using urllib and then parse and extract the comment counts 
from the XML data, compute the sum of the numbers in the file.
'''

import urllib.request
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    url = input('Enter URL: ')
    if len(url) < 1:
        break

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')

    tree = ET.fromstring(data)

    # Find all <count> tags
    counts = tree.findall('.//count')
    
    # Extract the numbers and compute the sum
    total_sum = sum(int(count.text) for count in counts)
    
    print('Sum:', total_sum)
