import tweepy
from textblob import TextBlob as tb
import io

#Authenticate Twitter
consumer_key='get your own'
consumer_secret='yea right'

access_token='353087817-N6dNNiOhiSaehTGrLUX8kvqTYEPMyuwe745vndwe'
access_token_secret='sQ1RVuzfusCHVprAkqPs98p5IS12Lj9MFoMQHmcjL7ETY'

auth=tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api=tweepy.API(auth)

public_tweets=api.search("Pepsico")

for tweet in public_tweets:
    analysis=tb(tweet.text)
    file=io.open("tweetFile.csv","a",encoding="utf-8")
    file.write(tweet.text + "\n")
    if analysis.sentiment.polarity > 0.15:
        file.write("Positive Tweet \n")
    file.write("Negative Tweet \n")
    file.close()
    print(analysis.sentiment)
