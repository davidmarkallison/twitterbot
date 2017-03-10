import tweepy   # Twitter bot API - downloaded from GitHub
import sys      # For command line arguments
import os       # For directory navigation
import re       # For String manipulation
import time     # For sleep function

# Navigating to the current file's directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Opening the Silmarillion text file
sim_file = open(os.path.join(__location__, 'simdog.txt'));

# Opening the Silmarillion textfile
#sim_file = open("simdog.txt", "r")

# Reading the file and setting as a string
simdog = sim_file.read()

# Splitting the string around the full stops and creating an array
sim_arr = simdog.split(".")

# # If not all keys are given in arguments, kill script
# if len(sys.argv) < 5:
#     sys.exit("One or more keys/tokens not set.")
#
# # Consumer keys and access tokens, used for OAuth
# consumer_key = sys.argv[1]
# consumer_secret = sys.argv[2]
# access_token = sys.argv[3]
# access_token_secret = sys.argv[4]
#
# # OAuth process, using the keys and tokens
# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# # Creation of the actual interface, using authentication
# api = tweepy.API(auth)

i = 0
while True:
    pre_tweet = sim_arr[i]
    tweet1 = ""
    tweet2 = ""
    tweet3 = ""
    tweet4 = ""
    tweet5 = ""
    tweet6 = ""

    # Sample method, used to update a status
    if len(pre_tweet) < 140 and len(pre_tweet) > 1:
        print(pre_tweet) #api.update_status(pre_tweet)
    else:
        k = pre_tweet.rfind(" ")
        tweet1 = pre_tweet[:k]

    print(pre_tweet)
    print(tweet1)
    print(tweet2)

    i = i + 1

    time.sleep(1)
