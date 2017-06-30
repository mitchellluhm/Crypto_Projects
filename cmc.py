import bs4
from urllib.request import urlopen
from bs4 import BeautifulSoup
import time

url = 'https://coinmarketcap.com/'

def rm_end(s):
	clean_s = ""
	i = 0
	while (s[i].isdigit()):
		clean_s += s[i]
		i += 1
	return clean_s

while (True):
	uClient = urlopen(url)
	page_html = uClient.read()
	uClient.close()

	page_soup = BeautifulSoup(page_html, "html.parser")

	# ignore index 0.
	# 1 to 100 are top 100 coins
	coins = page_soup.find_all('tr')
	coins = coins[1:]


	for coin in coins:

		c = coin.find_all('a')

		name = c[0].text.replace("/", "")
		price = c[1].text[1:].replace(",", "")
		cir_sup = rm_end(c[2].text.strip().replace(",", ""))
		vol_24h = c[3].text.replace(",", "")[1:]

		filename = 'crypto_data/' + name + '.csv'
		tclock = time.strftime("%H:%M:%S")
		tdate = time.strftime("%m/%d/%Y")

		f = open(filename, "a+")
		f.write(str(price) + ", " + str(cir_sup) + ", " + str(vol_24h) + ", ")
		f.write(str(tclock) + ", " + str(tdate) + "\n")
		f.close()

	time.sleep(1800)
