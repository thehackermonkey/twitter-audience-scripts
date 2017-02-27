import pymongo
from pymongo import MongoClient
import socialcrawler

client = MongoClient()
db = client['twitter']
mapsfollowers = db['mapsfollowers']

count = 0 

for follower in mapsfollowers.find():
	if 'link' in follower.keys():
		websitedata = socialcrawler.getsitedata(follower['link'])
		if not websitedata:
			print('not data')
			continue
		else: 
			follower_id = follower['_id']
			db.mapsfollowers.update_one({'_id': follower_id}, {"$set": {"website_links": websitedata}})
			count +=1
			print('inserted ' + str(count))


