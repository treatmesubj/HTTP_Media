import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup, element

session = requests.session()

# find latest post
html = session.get("http://n-gate.com/").text
soup = BeautifulSoup(html, "html.parser")
div_main = soup.select_one("div[id='main-copy']")
latest_blog_href = div_main.select_one("h1 a").attrs["href"]

# go to latest post
html = session.get(f"http://n-gate.com/{latest_blog_href}").text
soup = BeautifulSoup(html, "html.parser")
div_main = soup.select_one("div[id='main-copy']")
blog_title = div_main.select_one("h1").text
blog_desc = div_main.select_one("p").text
story_elems = soup.select("div[id='main-copy'] p")[1:]

# get ascii art for blog title
print(blog_title)
print(blog_desc, end="\n\n")

for story in story_elems:
    story_soup = BeautifulSoup(str(story), "html.parser")
    for child in story_soup.select_one("p").children:
        if type(child) is element.Tag:
            if "style" in child.attrs or child.name == "i":
                pass
            else:
                child.decompose()
    try:
        title = story.select_one("span a").text
        link = story.select_one("span.storylink a").attrs["href"]
        date = story.select_one("span.smalldate").text
        comments = story.select_one("span.small a").attrs["href"]
        print(f"[{date} | {title} | {link} | {comments}]\n")
    except AttributeError:
        pass
    except Exception:
        print(story, end="\n\n\n")

    annotation = story_soup.text.strip()
    if len(annotation) != 0:  # ngate messin stuff up
        print(annotation, end="\n\n\n")
