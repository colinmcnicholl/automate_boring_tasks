#! python3
# imageSiteDownloader.py - Goes to photo sharing site, imgur searches for a category of photos, and then downloads all the resulting images.

import requests, os, bs4

url = 'https://imgur.com/search?q=mourne%20mountains'
os.makedirs('imgur', exist_ok=True)

print('Downloading page %s...' % url)
res = requests.get(url)
res.raise_for_status()

soup = bs4.BeautifulSoup(res.text, 'lxml')
postElem = soup.select('a img')
if postElem == []:
	print('Could not find the posts images.')
else:
	for i in range(len(postElem)):
		postUrl = 'http:' + postElem[i].get('src')
		print('Downloading iamge %s...' % (postUrl))
		res = requests.get(postUrl)
		res.raise_for_status()
		imageFile = open(os.path.join('imgur', os.path.basename(postUrl)), 'wb')
		for chunk in res.iter_content(100000):
			imageFile.write(chunk)
		imageFile.close()
		
	print('Done.')


