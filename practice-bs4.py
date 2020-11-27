from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
page = response.text
soup = BeautifulSoup(page, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
	text = article_tag.getText()
	link = article_tag.get("href")
	article_texts.append(text)
	article_links.append(link)

article_points = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_points = article_points.index(max(article_points))
max_article_text = article_texts[max_points]
max_article_link = article_links[max_points]
print(article_texts)
print(article_links)
print(article_points)
print(f"\ntop article with {max(article_points)} points:\n")
print(max_article_text)
print(max_article_link)

# import lxml
#
# with open("website.html") as file:
# 	contents = file.read()
#
# soup = BeautifulSoup(contents, 'html.parser')
# anchorTags = soup.find_all("a")
# print(anchorTags)

# for tag in anchorTags:
# 	print(tag.getText())
# 	print(tag.get("href"))

# heading = soup.find(name="h1", id='name')
# print(heading)

# formTag = soup.find('form')
# maxSize = formTag.get("maxsize")
# print(maxSize)


# url = soup.select(selector='p a')
# print(url)

