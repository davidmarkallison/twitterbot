import tweepy   # Twitter bot API - downloaded from GitHub
import sys      # For command line arguments
import os       # For directory navigation

# Navigating to the current file's directory
__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Opening the Silmarillion text file
sim_file = open(os.path.join(__location__, 'simdog.txt'));

# Reading the file and setting as a string
simdog = sim_file.read()

# Splitting the string around the full stops and creating an array
sim_arr = simdog.split(".")

# Prints longest sentence in the text file
print(max(len(x) for x in sim_arr))
