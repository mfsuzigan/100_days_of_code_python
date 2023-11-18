import re

import requests
from bs4 import BeautifulSoup

# local file
# with open("website.html") as file:
#     soup = BeautifulSoup(file.read(), "html.parser")

# experimenting with bulk downloads
# page_number = 11
# models_request = requests.get("h", params={"page": page_number})
# content = BeautifulSoup(models_request.content, "html.parser")
#
# for img in content.find_all("img", src=re.compile("profile")):
#     img_name = f"{img.attrs['title']}.jpg"
#     with open(img_name, "wb") as img_file:
#         print(f"writing {img_name}")
#         img_file.write(requests.get(img.attrs["src"]).content)

# ycombinator hacker news
soup = BeautifulSoup(requests.get("http://news.ycombinator.com").content, "html.parser")
article = soup.find_all(class_="titleline")[0]
upvote_count = soup.find_all(class_="score")[0]
link = article.findNext(name="a").attrs["href"]

print(f"First article is \"{article.text}\", upvote is {upvote_count.text}, link is {link}")

upvote_count_list = [int(score.text.split(" ")[0]) for score in soup.find_all(class_="score")]
max_upvote = max(upvote_count_list)
max_upvote_index = upvote_count_list.index(max_upvote)
max_upvote_article_title = soup.find_all(class_="titleline")[max_upvote_index].text

print(f"Most popular article ({max_upvote} votes) is \"{max_upvote_article_title}\"")

# for title in articles:
#     print(title.text)
