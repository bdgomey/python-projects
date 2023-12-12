import requests



r = requests.get("https://newsapi.org/v2/everything?qInTitle=nba%20basketball&from=2023-11-12&to=2023-12-12&sortBy=popularity&language=en&apiKey=19b4b874b94c49edb0886cb7b0ef02e0")

content = r.json()
articles = (content["articles"])

print(type(articles))


for article in articles:
  news = article['title']
  if "lakers" in news.lower():
    print (news)
  else:
    continue
