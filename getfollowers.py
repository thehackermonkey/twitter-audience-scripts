from TwitterAPI import TwitterAPI
from TwitterAPI import TwitterRestPager
from config import secrets
import pymongo
from pymongo import MongoClient

# DB conection
client = MongoClient()
db = client['twitter']
mapsfollowers = db.mapsfollowers

#twitter api
api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)

#twitter query
query = {'user_id' : 2835564560,
		'count': 50
	}

r = TwitterRestPager(api, 'followers/list', query)


count = 0
#DB insert 
for user in r.get_iterator():
	count +=1
	data ={}
	data['name'] = user['name']
	data['user_name'] = user['screen_name']
	data['default_profile_image'] = user['default_profile_image']
	data['user_id'] = user['id']
	data['description'] = user['description']
	data['location'] = user['location']
	data['followers'] = user['followers_count']
	data['following'] = user['friends_count']
	data['lang'] = user['lang']
	data['tweets'] = user['statuses_count']
	entities = user['entities']
	if 'url' in entities.keys() :
		url = entities['url']
		urls = url['urls']
		link = urls[0]['expanded_url']
		data['link'] = link
	mapsfollowers.insert(data)
	print(count)


print('finished')
