import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
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
