import requests
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