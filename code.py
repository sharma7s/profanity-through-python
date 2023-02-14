import re

# read the tweets file
with open('tweets.txt', 'r') as f:
    tweets = f.readlines()

# read the set of racial slurs
with open('racial_slurs.txt', 'r') as f:
    racial_slurs = set([line.strip() for line in f])

# define a function to calculate the degree of profanity
def calculate_profanity(tweet):
    words = re.findall(r'\w+', tweet.lower())
    num_slurs = sum([1 for word in words if word in racial_slurs])
    profanity_score = num_slurs / len(words)
    return profanity_score

# loop through each tweet and calculate its degree of profanity
for tweet in tweets:
    profanity_score = calculate_profanity(tweet)
    print(f'{tweet.strip()} - profanity score: {profanity_score:.2f}')
