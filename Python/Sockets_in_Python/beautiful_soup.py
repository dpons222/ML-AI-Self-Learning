from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

'''
find span tags, find sum of the contents
'''


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

total_sum = 0
tags = soup('span')

for tag in tags:
    content = tag.text.strip()
    nums = int(content)
    total_sum += nums
print("total sum is",total_sum)