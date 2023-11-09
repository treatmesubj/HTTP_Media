#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
from rich import pretty, print

pretty.install()

res = requests.get("https://news.ycombinator.com")
soup = BeautifulSoup(res.text, "html.parser")

post_elems = soup.select(".titleline")
subtext_elems = soup.select(".subtext")


def sort_news_by_votes(news_info):
    return sorted(news_info, key=lambda k: k["points"], reverse=True)


def get_news_info(post_elems, subtext_elems):
    news_info = []

    for index, elem in enumerate(post_elems):
        title = post_elems[index].getText()
        story_link = post_elems[index].select_one("a[href]").get("href", None)
        try:
            points = int(
                subtext_elems[index].select_one(".score").getText().strip(" points")
            )
        except AttributeError:
            points = None
        try:
            comments_link = (
                subtext_elems[index].select_one("a[href*='item']").get("href", None)
            )
        except AttributeError:
            comments_link = None

        if points:
            news_info.append(
                {
                    "title": title,
                    "story_link": story_link,
                    "points": points,
                    "comments_link": f"https://news.ycombinator.com/{comments_link}",
                }
            )

    return sort_news_by_votes(news_info)


if __name__ == "__main__":
    news_info = get_news_info(post_elems, subtext_elems)
    for post in news_info:
        print(f"[{post['points']}]: {post['title']}")
        print(f"story: {post['story_link']}")
        print(f"comments: {post['comments_link']}\n")
