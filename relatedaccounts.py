## We can expand the inmediate search area by looking at the twitter description of the user
## and extracting other twitter accounts 

from textblob import TextBlob
import pymongo
from pymongo import MongoClient
import re

client = MongoClient()
db = client['twitter']
mapsfollowers = db['mapsfollowers']

#tw-usr regex
twitter_user = re.compile('@[a-zA-Z0-9_-]+')
bad_ending_punctuation = ['.',',',';',':']

def getRelatedAccounts(desc):
	description = TextBlob(desc)
	words = description.split()
	related_accounts = []
	for word in words:
		if twitter_user.match(word):
			if word[-1] in bad_ending_punctuation:
				word = word[:-1]
				related_accounts.append(word)
			else:
				related_accounts.append(word)
	if related_accounts:
		return related_accounts


for follower in mapsfollowers.find():
	if 'description' in follower.keys():
		id = follower['_id']
		related = getRelatedAccounts(follower['description'])
		if related:
			db.mapsfollowers.update_one({'_id': id}, {"$set": {"related_to":related}})


