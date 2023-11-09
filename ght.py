#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup


if __name__ == "__main__":
    html = requests.get("https://github.com/trending?since=weekly").text
    soup = BeautifulSoup(html, "html.parser")

    for proj_elem in soup.select("article"):
        title = []
        link = ""
        lang = ""
        desc = ""

        title_elem = proj_elem.select_one("h2 a")
        if title_elem:
            title = f"{[x.strip() for x in title_elem.text.split('/')]}"
            link = f"https://github.com{title_elem.attrs['href']}"

        lang_elem = proj_elem.select_one("span[itemprop='programmingLanguage']")
        if lang_elem:
            lang = lang_elem.text

        desc_elem = proj_elem.select_one("p")
        if desc_elem:
            desc = desc_elem.text.strip()

        print(f"{title} {lang}")
        print(link)
        print(f"{desc}\n")
