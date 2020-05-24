import requests
# from requests_html import HTML
from bs4 import BeautifulSoup

html = requests.get("https://github.com/trending/python?since=daily").text
soup = BeautifulSoup(html, 'html.parser')

for proj in soup.select("article"):
	title = proj.select_one("h1 a")
	desc = proj.select_one("p")
	print(f"{[x.strip() for x in title.text.split('/')]}")
	print(f"https://github.com{title.attrs['href']}")
	try:
		print(f"{desc.text.strip()}")
	except AttributeError:
		pass
	print("\n")