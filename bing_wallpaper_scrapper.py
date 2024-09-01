from lxml import html
import requests
import urllib3
from bs4 import BeautifulSoup
import os
import shutil
import datetime
from win10toast import ToastNotifier
import re


url = 'http://www.bing.com'
http = urllib3.PoolManager()
response = http.request('GET', url)
soup = BeautifulSoup(response.data.decode('utf-8'), 'html.parser')

'''
print(soup.prettify())
for link in soup.find_all('a'):
    print(link.get('href'))
print soup
'''

str1 = 'http://www.bing.com'
strmid = soup.select_one('#preloadBg').prettify()
print('1*'+strmid)
str2mid = strmid.replace('<link as="image" href="/th?id=OHR.','')
print('2*'+str2mid+'\n')
str2mid = re.sub(r'.webp','.jpg',str2mid)
str2 = re.sub(r'&amp;qlt=50" id="preloadBg" rel="preload"/>\n','',str2mid)
print('3*'+str2+'\n')
'''
images = soup.findAll('img')
for image in images:
    #print image['src']
    str2 = image['src']
'''

bing_image_url = str1 + '/th?id=OHR.' + str2
print('4*'+bing_image_url+'\n')
dtn = str(datetime.datetime.now())
print('5*'+dtn[0:-10]+'\n')


path = os.path.abspath("PATH/"+str2)
print('6*'+path)
with http.request('GET', bing_image_url, preload_content=False) as r, open(path, 'wb') as out_file:       
    shutil.copyfileobj(r, out_file)

os.system('"'+path+'"')

toaster = ToastNotifier()
toaster.show_toast("Bing Scrapper",str2[:-28]+" @ "+dtn[0:-10])

