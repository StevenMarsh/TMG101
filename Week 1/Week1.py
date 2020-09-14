import pandas as pd

filename = "covid19_tweets.csv"

dataframe = pd.read_csv(filename)

# print(dataframe.head(5)) #print first 5 rows
#
# print(dataframe.tail(5)) #print last 5 rows
#
# print(dataframe.columns) #print name of column headers
#
# print(dataframe['user_followers'].describe()) #get statistics on specified headers



#TODO

#1. Find the average number of followers that verified users have






#2 Look up numpy, import that library to this file. Replace all rows whose user_follower count is 0 with the average
#number of followers (Look at image in folder to see ways of dealing with missing/bad values)


#2. Get some cool statistic (like #1), put it in a function and then use that function to assign a value to a variable
# and print out that variable
