import tweepy   # Twitter bot API - downloaded from GitHub
import sys      # For command line arguments
import os       # For directory navigation
import re       # For String manipulation
import time     # For sleep function
import math

# Navigating to the current file's directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Opening the Silmarillion text file
sim_file = open(os.path.join(__location__, 'simdog.txt'))

# Opening the Silmarillion textfile
#sim_file = open("simdog.txt", "r")

# Reading the file and setting as a string
simdog = sim_file.read()

# Splitting the string around the full stops and creating an array
sim_arr = simdog.split(".")

# # If not all keys are given in arguments, kill script
if len(sys.argv) < 5:
     sys.exit("One or more keys/tokens not set.")
#
# # Consumer keys and access tokens, used for OAuth
consumer_key = sys.argv[1]
consumer_secret = sys.argv[2]
access_token = sys.argv[3]
access_token_secret = sys.argv[4]
#
# # OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
#
# # Creation of the actual interface, using authentication
api = tweepy.API(auth)

i = 0
while True:
    pre_tweet = sim_arr[i]
    tweets = ["","","","","",""]


    pre_tweet = pre_tweet.split(" ")
    for word in pre_tweet:
        if len(tweets[0] + word + " ") < 140 and tweets[1] == "":
            tweets[0] += word + " "
        elif len(tweets[1] + word + " ") < 140 and tweets[2] == "":
            tweets[1] += word + " "
        elif len(tweets[2] + word + " ") < 140 and tweets[3] == "":
            tweets[2] += word + " "
        elif len(tweets[3] + word + " ") < 140 and tweets[4] == "":
            tweets[3] += word + " "
        elif len(tweets[4] + word + " ") < 140 and tweets[5] == "":
            tweets[4] += word + " "
        elif len(tweets[5] + word + " ") < 140:
            tweets[5] += word + " "  
    
    for tweet in tweets:
        if tweet == "":
            continue
        else:
            api.update_status(tweet)
            print(tweet + "\n")
            time.sleep(60)
    
    i = i + 1
    #keeps counter variable in file in case of need to shut down we can re-start from where we left off.
    f = open(os.path.join(__location__, 'counter-perm.txt'), 'w')
    f.write(str(i))
    f.close()

    time.sleep(3600)
