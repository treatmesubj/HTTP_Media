import requests
from requests_html import HTML
import sys

"""
fetches /r/whatstheword/top/ and allows you to choose a post to read its comments
"""

if __name__ == "__main__":

	tf_options = {
		"1hr": "?sort=top&t=hour",
		"24hrs": "?sort=top&t=day",
		"week": "?sort=top&t=week"
	}

	if len(sys.argv)  > 1:
		if sys.argv[1] in list(tf_options.keys()):
			tf_choice = sys.argv[1]
		else:
			print(f"{sys.argv[1]} is invalid option. Choose from {list(tf_options.keys())}")
	else:
		tf_choice = "24hrs"

	posts_html = HTML(html=requests.get(f"https://old.reddit.com/r/whatstheword/top/{tf_options[tf_choice]}", 
		headers={"user-agent": "Mozilla/5.0"}).text)
	posts = posts_html.find("div.top-matter p.title > a[href*='/r/']")

	print(f"[Top Posts in past {tf_choice}]: ")
	for num, post in enumerate(posts):
		print(f"({num}): {post.text}")

	post_choice = int(input("\npost choice (num): "))
	post_link = f"https://old.reddit.com{[link for link in posts[post_choice].links][0]}"

	comments_html = HTML(html=requests.get(post_link,
		headers={"user-agent": "Mozilla/5.0"}).text)

	# link
	print(f"\n\n{post_link}")
	# title
	print(f"{posts[post_choice].text}")
	# body
	try:
		print(comments_html.find("div[class*='top-matter'] ~ div p")[0].text, "\n")
	except IndexError:
		pass # no body

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
			
			if (len(points_elems) != 0) and ("I am a bot" not in comment):
				points = points_elems[0].attrs['title']
				print(f"[{points} point(s)]: {comment}")

		print("+"*discussion)