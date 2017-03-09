import tweepy

sim_file = open("simdog.txt", "r")
simdog = sim_file.read()

sim_arr = simdog.split(".")

print(len(sim_arr))