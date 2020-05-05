import requests

def get_urls(queryString, country):
	res = requests.get(url=f"https://itunes.apple.com/search?term={queryString}&entity=album&country={country}")
	imgs = dict()
	for i in res.json()['results']:
		imgs[i['collectionId']] = [i['artworkUrl100'].replace('100x100bb.jpg', "10000x10000bb.png"),
								   i['artworkUrl100'],
								   i['collectionName'],]
								   
	return imgs
	