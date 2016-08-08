import requests
from bs4 import BeautifulSoup

def prettify(url):
	connect = requests.get(url)
	data = connect.content
	soup = BeautifulSoup(data, "html.parser")
	prety = soup.prettify
	return prety

def scrapText(url, tag, classIdentity=False, className=False):
	connect = requests.get(url)
	data = connect.content
	soup = BeautifulSoup(data, "html.parser")
	get_tags = soup.find_all(tag, {classIdentity : className})
	tolist = []
	for data in get_tags:
		tolist.append(data.text)
	return (tolist)


