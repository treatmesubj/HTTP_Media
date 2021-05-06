import requests
from requests_html import HTML
from rich import pretty, print, traceback; pretty.install(); traceback.install();

"""
fetches /r/whatstheword/top/ and allows you to choose a post to read its comments
"""

tf_options = {
	"1hr": "?sort=top&t=hour",
	"24hrs": "?sort=top&t=day",
	"week": "?sort=top&t=week"
}
print(list(tf_options.keys()))
tf_choice = input(f"select time frame: ")

posts_html = HTML(html=requests.get(f"https://old.reddit.com/r/whatstheword/top/{tf_options[tf_choice]}", 
	headers={"user-agent": "Mozilla/5.0"}).text)
posts = posts_html.find("div.top-matter p.title > a[href*='/r/']")

print("[posts]: ")
for num, post in enumerate(posts):
	print(f"({num}): {post.text}")

post_choice = int(input("\npost choice (num): "))

comments_html = HTML(html=requests.get(f"https://old.reddit.com{[link for link in posts[post_choice].links][0]}",
	headers={"user-agent": "Mozilla/5.0"}).text)

# title
print(f"\n\n{posts[post_choice].text}")
# body
print(comments_html.find("div[class*='top-matter'] ~ div p")[0].text, "\n")
# comments
threads = comments_html.find("div.commentarea > div.sitetable > div[data-type='comment']")
for thread in threads:
	comment_sections = thread.find("div.entry")
	
	discussion = 0
	if len(comment_sections) > 1:
		discussion = 40
		print("+"*discussion)
	
	for comment_section in comment_sections:
		comment = comment_section.find("form")[0].text
		points_elems = comment_section.find("p.tagline span[class='score unvoted']")
		
		if len(points_elems) != 0:
			points = points_elems[0].attrs['title']
			print(f"({points}): {comment}")

	print("+"*discussion)