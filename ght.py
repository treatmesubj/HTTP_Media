import requests
import platform

if platform.system() == 'Windows':
	from requests_html import HTML

	html = HTML(html=requests.get("https://github.com/trending/python?since=daily").text)

	for proj in html.find("article"):
		title = proj.find("h1 a", first=True)
		desc = proj.find("p", first=True)
		print(f"~~~{title.text}~~~", " {")
		print(f"	https://github.com{title.attrs['href']}")
		try:
			print(f"	{desc.text}")
		except AttributeError:
			pass
		print("}", end="\n\n")

if platform.system() == 'Linux':
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
