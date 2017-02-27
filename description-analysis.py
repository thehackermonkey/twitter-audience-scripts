##analyzing twitter descriptions to discover interesting data from the audience.
import operator
import pymongo
from pymongo import MongoClient
from textblob import TextBlob

client = MongoClient()
db = client['twitter']
mapsfollowers = db['mapsfollowers']


allwords = []

def getDescriptionWords(x):
	description = TextBlob(x['description'])
	return description.noun_phrases

for follower in mapsfollowers.find():
	if 'description' in follower.keys():
		allwords.append(follower['description'])

blobAll = TextBlob(str(allwords).lower())
sentences = blobAll.noun_phrases

results = {}

for sentence in sentences:
	if sentence not in results.keys():
		results[str(sentence)] = sentences.count(sentence)

sorted_results = sorted(results.items(), key=operator.itemgetter(1))

## A sorted dictionary of the most used "noun phrases" describing the audience
## Spoiler Alert : No1 = "aerial photography". I think this can be used to find similar audiences
print(sorted_results)








