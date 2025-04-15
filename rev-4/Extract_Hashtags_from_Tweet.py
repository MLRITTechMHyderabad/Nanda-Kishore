import re

tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

hashtag_pattern = r'#\w+'

hashtags = re.findall(hashtag_pattern, tweet)

print(hashtags)
