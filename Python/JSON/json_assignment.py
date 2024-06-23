import urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors (if needed)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')


print('Retrieving', url)
uh = urllib.request.urlopen(url, context=ctx)
data = uh.read().decode()
print('Retrieved', len(data), 'characters')

js = json.loads(data)


total_sum = sum(item['count'] for item in js['comments'])

print('Sum:', total_sum)
