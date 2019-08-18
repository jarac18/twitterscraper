import requests
from bs4 import BeautifulSoup

#curl twitter.com/search

url = "https://twitter.com/search?q=joe%20rogan&src=tyah"
results = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0"})
soup = BeautifulSoup(results.text, "html.parser")

users = soup.select("a.js-user-profile-link b")  # list of html elements
for user in users:
   print("USER:", user.get_text(), file=open("twitter.txt", "a"))

tweets = soup.select("p.tweet-text")
for tweet in tweets:
   print("TWEET:", tweet.get_text(), file=open("twitter.txt", "a"))

hashtags = soup.select("a.twitter-hashtag b")
for hashtag in hashtags:
    print("HashTag:", hashtag.get_text(), file=open("twitter.txt", "a"))

