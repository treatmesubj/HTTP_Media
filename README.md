# Hacker News
Fetch the front page of Hacker News

```
PS [rock] [C:] ...\HTTP_Media> python .\hacker_news.py
[713]: I fought the PayPal and I won (jessesingal.substack.com)
story: None
comments: https://news.ycombinator.com/item?id=33462658

[614]: Twitter’s mass layoffs have begun (techcrunch.com)
story: None
comments: https://news.ycombinator.com/item?id=33463908

[441]: Privately-Owned Rail Cars (amtrak.com)
story: None
comments: https://news.ycombinator.com/item?id=33460052

[315]: Tinygrad: A simple and powerful neural network framework (tinygrad.org)
story: None
comments: https://news.ycombinator.com/item?id=33462337

[216]: Low Energy Chest Fridge (notechmagazine.com)
story: None
comments: https://news.ycombinator.com/item?id=33463683
```

# N-Gate
Ironically read the n-gate's latest post, most likely an annotated digest of the top "Hacker" "News" posts

```
PS [rock] [C:] ...\HTTP_Media> python .\ngate.py
webshit weekly
An annotated digest of the top "Hacker" "News" posts for the second week of August, 2021.


[August 08, 2021 | One Bad Apple | https://www.hackerfactor.com/blog/index.php?/archives/929-One-Bad-Apple.html | http://news.ycombinator.com/item?id=28110159]

An Internet is mad about Apple (business model: "Uber for spyware") turning your phone into a cop, and posts a lot of irrelevant misunderstandings about it.  Hackernews follows this up with dire warnings about the state of child trafficking in the world today, complete with admonishments that there is no hope for improvement, except for venture-backed smartphone apps.
```

# /r/whatstheword
Fetches /r/whatstheword/top/ and allows you to choose a post to read its comments

Usage: `python wtw.py [1hr | 24hrs | week]`

```
PS [rock] [C:] ...\HTTP_Media> python .\wtw.py
[Top Posts in past 24hrs]:
(0): WTW for a supervising adult at a kids party.
(1): WTW for when you completely give up on something (or deliberately keep on making mistakes) because you made a small mistake?
(2): WTW for Understanding of the sacredness of life or something?
(3): WTW for an intense fear of windows.
```

```
post choice (num): 0

https://old.reddit.com/r/whatstheword/comments/ylggjs/wtw_for_a_supervising_adult_at_a_kids_party/
WTW for a supervising adult at a kids party.
Thought starters;

++++++++++++++++++++++++++++++++++++++++
[166 point(s)]: Chaperone?
[36 point(s)]: !solved
[7 point(s)]: Olden day word.
Huh?
```

# Github Trending
Gathers the week's trending repositories on Github and displays brief info about them

```
PS [rock] [C:] ...\HTTP_Media> python .\ght.py
['openai', 'openai-cookbook']
https://github.com/openai/openai-cookbook
Examples and guides for using the OpenAI API


['microsoft', 'unilm']
https://github.com/microsoft/unilm
Large-scale Self-supervised Pre-training Across Tasks, Languages, and Modalities
```
