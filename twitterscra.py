import requests
from bs4 import BeautifulSoup

#curl twitter.com/search
url = "https://twitter.com/search?q=joe%20rogan&src=tyah"
results = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:68.0) Gecko/20100101 Firefox/68.0"})

soup = BeautifulSoup(results.text, "html.parser")
#print(soup.prettify())

#extract username
users = soup.select("a.js-user-profile-link b")     #list of html elements
#When using 'select' it returns a list.  have to pull element out of the list

for user in users:
    print(user.get_text())

#print(results.text) #test code

#extract tweets
tweets = soup.select("p.tweet-text")

for tweet in tweets:
    print(tweet.get_text())


#extract pictures
