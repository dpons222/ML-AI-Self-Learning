import urllib.request
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Initial URL
url = input('Enter URL: ')
pos = 18
counts = 7


for i in range(counts):
    # Open the URL, read the HTML content, parse
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")

    # Retrieve anchor tags
    tags = soup('a')

    # Retrieve the href value at the specified position
    link = tags[pos - 1].get('href', None)
    if link is None:
        print("No href attribute found for the tag at the specified position.")
        break

    # Update the URL to the next link to follow
    url = link
    print(f"Following link {i}: {url}")


#print last name
last_name = url.split('_')[-1]
print("The last name is:", last_name)
