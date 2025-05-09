from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
response.raise_for_status()
# print(response.text)

soup = BeautifulSoup(response.text, "html.parser")
# print(soup.prettify())

# print(soup.find(name="title").text)
# print(soup.title.text)

# article_tag = soup.select_one(selector=".title a")
# print(f"Tag: {article_tag}")
#
# article_tag_text = article_tag.getText()
# print(f"Text: {article_tag_text}")
#
# article_tag_link = article_tag.get("href")
# print(f"Link : {article_tag_link}")
#
# article_updoots = soup.select_one(selector=".score").getText()
# print(f"Updoots: {article_updoots}")

article_texts = []
article_links = []

articles = soup.select(selector=".titleline > a")
for article in articles:
    # print(article)
    article_text = article.getText()
    # print(f"Text: {article_text}")
    article_texts.append(article_text)

    article_link = article.get("href")
    # print(f"Link : {article_link}")
    article_links.append(article_link)

# article_updoots = [int(score.getText().split(' ')[0]) for score in soup.select(selector=".score")]

article_updoots = []
subtexts = soup.find_all(name="td", class_="subtext")
for subtext in subtexts:
    if not subtext.find(name="span", class_="score"):
        article_updoots.append(0)
    else:
        article_updoots.append(int(subtext.find(name="span", class_="score").getText().split()[0]))

print(article_links)
print(article_texts)
print(article_updoots)

most_updoots = max(article_updoots)
print(f"Most updoots: {most_updoots}")
most_updoots_index = article_updoots.index(most_updoots)
print(most_updoots_index)

print(f"Most updooted article: {article_texts[most_updoots_index]}, link: {article_links[most_updoots_index]}")
