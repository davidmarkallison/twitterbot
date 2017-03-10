import tweepy
import os

sim_file = open("simdog.txt", "r")
simdog = sim_file.read()

sim_arr = simdog.split(".")

print(sim_arr[1])

# # Consumer keys and access tokens, used for OAuth
# consumer_key = ''
# consumer_secret = ''
# access_token = ''
# access_token_secret = ''
#
# # OAuth process, using the keys and tokens
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# # Creation of the actual interface, using authentication
# api = tweepy.API(auth)
#
# tweet = ""
# # Sample method, used to update a status
# if len(tweet) < 140 || len(tweet) > 0:
#     api.update_status(tweet)
