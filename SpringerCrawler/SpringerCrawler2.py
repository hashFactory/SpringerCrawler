from bs4 import BeautifulSoup, SoupStrainer
from urllib.request import urlopen
from urllib.error import URLError, HTTPError
import re

list_of_books = []
doi = []
prices = []
filename = "doiandname8.txt"
filename_2 = "doi8.txt"

def fetch(number):
	try:
		html = urlopen("http://www.springer.com/us/product-search/discipline?disciplineId=mathematics&facet-categorybook=categorybook__pcytextbook&facet-lan=lan__en&facet-type=type__book&page=" + str(number) + "&returnUrl=us%2Fmathematics&topic=M00009%2CM11000%2CM11019%2CM11027%2CM11035%2CM11043%2CM11051%2CM1106X%2CM11078%2CM11086%2CM11094%2CM11100%2CM11116%2CM11124%2CM11132%2CM12007%2CM12015%2CM12023%2CM12031%2CM1204X%2CM12058%2CM12066%2CM12074%2CM12082%2CM12090%2CM12112%2CM12120%2CM12139%2CM12147%2CM12155%2CM12163%2CM12171%2CM1218X%2CM12198%2CM1221X%2CM12220%2CM13003%2CM13011%2CM13038%2CM13062%2CM13070%2CM13080%2CM13090%2CM13100%2CM13110%2CM13120%2CM13130%2CM13140%2CM1400X%2CM14018%2CM14026%2CM14034%2CM14042%2CM14050%2CM14068%2CM14070%2CM21006%2CM21014%2CM21022%2CM21030%2CM21040%2CM21050%2CM23009%2CM24005%2CM24010%2CM25001%2CM26008%2CM26016%2CM26024%2CM26030%2CM26040%2CM27004%2CM27010%2CM28000%2CM28019%2CM28027%2CM29000%2CM29010%2CM29020%2CM31000%2CM31010%2CM31020%2CM32000%2CM33000%2CM34000%2CM35000")
	except HTTPError:
		return
	if (html.getcode() == 404):
		return
	html2 = html.read().decode("utf-8")

	soup = BeautifulSoup(html2, parse_only=SoupStrainer('a'))

	print("Page " + str(number))
	for link in soup:
		if link.has_attr('href'):
			if "/us/book/" in link['href']:
				if not ("http://www.springer.com" + link['href']) in list_of_books:
					list_of_books.append("http://www.springer.com" + link['href'])

def fetch_doi(url, track):

	try:
		html = urlopen(url)
	except HTTPError:
		return
	if (html.getcode() == 404):
		return
	html2 = html.read().decode("utf-8")

	soup = BeautifulSoup(html2, parse_only=SoupStrainer('dd'))
	price_soup = BeautifulSoup(html2, 'html.parser')

	dd = soup.find_all('dd')

	book_name = soup.find('dd', itemprop="name").string

	print("Book: " + str(track) + "/" + str(len(list_of_books)) + "(" + str(100 * track / len(list_of_books)) + "%) Testing: " + url)
	print(book_name)
	price = price_soup.find("span", {"class": "price"}).string.replace("\n", "").replace(" ", "").replace("ca.", "")

	if "\n" not in price:
		print(price)

	for doi_code in dd:
		if (str(doi_code.string).startswith("10.")):
			doi.append("doi:" + doi_code.string)
			print("doi:" + str(doi_code.string))
			file2.write("doi:" + str(doi_code.string) + "\n")
			file.write(book_name + "\n")
			if len(price) > 2:
				file.write(price + "\n")
			file.write("doi:" + str(doi_code.string) + "\n")

file = open(filename, "w")
file2 = open(filename_2, "w")

for i in range(121, 145):
	fetch(i)

tracker = 0
for i in list_of_books:
	tracker += 1
	fetch_doi(i, tracker)

file.close()
file2.close()
