import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    html = requests.get("https://github.com/trending?since=weekly").text
    soup = BeautifulSoup(html, 'html.parser')

    for proj in soup.select("article"):

        title = proj.select_one("h1 a")
        if title:
            print(f"{[x.strip() for x in title.text.split('/')]}", end=" ")

        lang = proj.select_one("span[itemprop='programmingLanguage']")
        if lang:
            print(lang.text)
        else:
            print()

        print(f"https://github.com{title.attrs['href']}")

        desc = proj.select_one("p")
        if desc:
            print(f"{desc.text.strip()}")

        print("\n")

