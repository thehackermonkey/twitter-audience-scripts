# Finding information from the followers of an especific twitter account

### The challenge:

> Get as much info from a list of twitter users following an especific account


### The initial approach:

First we need to ensure the data we get is as reliable as we can and as low-intrusive as we can.

#### Brainstorming:

* Use the twitter user and try to find the same user on facebook
	* The good: A lot of people do this
	* The bad: This really doesn't get's me closer to the user. Also it's a guess and other person may have the same username on facebook (And I don't have a computer power cheap solution for this)

* Check thee twitter API and get all the interesting data we can get from there
	* The Good: This is extremly close to the user and may discover some interesting stuff (location, lang...)
	* URLS!

* A lot of people use twitter as their public business card, maybe we can get something interesting from the description ...

#### Conclussion: 

> Let's use the twitter account as an anchor for all the data we are going to look for so it's allways connected to this origin, we are going to start from the idea that a great ammount of twitter users use the platform as a digital business card.


My process:


1. Let's study the twitter api to find what we think may be useful

* Name
* Username
* Description (We are going to discover something interesting later)
* Location
* Languague (of the user's  twitter UI) 
* User ID (in case we want to follow the user activity)
* URL (This may be the most important part of a user profile)
* Default profile image (this may be useful if we want to filter active users)
* Following (Statistical data)
* Followers (Statistical data)
* Tweets (Statistical data)

... And draw a lot on the notebook.


2. Building the twitter API connection 

#### [getfollowers.py](getfollowers.py)

A python script to get all the users an account follows and save all the information on MongoDB.

> We obtained 527 twitter users following the provided account.

3. Build a set of python scripts to get the most data we can relate from twitter.

#### [crawler.py](crawler.py) and [socialcrawler.md](socialcrawler.md) 

We are going to use the public link (If any) from the user's profile and scrap the home page of that webpage looking for useful links (facebook, mail, linkedin) if we find any we are going to add it to the document of that user on Mongo. 


> We got *91* useful links from 254 users with url's on their profile. 


#### [relatedaccounts.py](relatedaccounts.py)

Maybe we can also find useful data on the description of the user profile. A lot of people use to mention where are they working at this moment or twitter accounts that are related with them.

> We got related accounts from *47* user 


#### [description-analysis.py](description-analysis.py)

¿Could be possible to get more from the user description?. If we analyzethe the text from the profile description we can get some data that we can use later defining and creating audiences.

> I did an analysis of the most common "noun phrases" in all the users descriptions and found out that the most common fields of interest of users are:

1. Aerial Photography
2. UAV's
3. Real Estate
4. Precision agriculture
5. Drone pilot
6. Tech geek
7. Drone enthusiast

### Next steps

I would:

* Improve the crawler so it looks not only for the home page but for the contact section (I'm pretty sure we can almost double the useful links if we do this)

* Maybe use [email hunter's api](https://hunter.io) to look for some missing emails. It's extremly easy to use [findemail.py](findemail.py)

* Use the same tecnique used with this followers with their related accounts.

* Add a field on the DB called "drone_related". We can accomplish this doing a little more analysis on the twitter descrption. (Creating a semantic dictionary of the public and filtering the descriptions)

* Create an api and a  front-end for this data so anyone on the company can perform queries and custom analysis that I'm missing.




