import re


def extract_hashtags(tweet):
    # Regex pattern for hashtags
    pattern = r'#\w+'

    # Find all matching hashtags
    hashtags = re.findall(pattern, tweet)

    return hashtags


# Example Input
tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

# Function call
result = extract_hashtags(tweet)
print(result)
