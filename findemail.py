## With enough resources the use of the Email Hunter API 
## could be a viable  and interesting option ()
import pymongo
from pymongo import MongoClient
from email_hunter import EmailHunterClient
client = EmailHunterClient('f4a32e429f31227d0be3b4195695b342fd14de1b')


client = MongoClient()
db = client['twitter']
mapsfollowers = db['mapsfollowers']


for follower in mapsfollowers.find():
	if 'link' in follower.keys():
		possible_emails = client.search(follower['link'])
		if possible_emails:
			follower_id = follower['_id']
			db.mapsfollowers.update_one({'_id': follower_id}, {"$set": {"website_possible_emails": websitedata}})

