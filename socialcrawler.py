# getting mail, facebbok and linkedin from homepages (to skycatch with love)
import urllib
import http
from http import client
from urllib import request, error, parse
import socket
from socket import timeout
from bs4 import BeautifulSoup
import re


def getsitedata(url):
	if url is None:
		return	
	try:
		request = urllib.request.Request(url)
		request.add_header('User-agent', 'Mozilla/5.0 (Linux i686)')
		html = urllib.request.urlopen(request,timeout= 8)
	except urllib.error.HTTPError:
		print('HTTPError')
		return
	except urllib.error.URLError:
		print('URLPError')
		return
	except urllib.error.ContentTooShortError:
		print('this shit was incomplete')
	except timeout:
		print('Timeout')
		return
	except socket.error:
		print('socket err')
		return
	except http.client.HTTPException:
		print('HTTPException')
		return
	# A hard except
	# except client.IncompleteRead:
	# 	print('incomplete read ')
	# 	return


	soup = BeautifulSoup(html ,  "html.parser")
	metadesc = soup.find(attrs={"name" : "description"})
	links = soup.find_all(href=re.compile("^https?:\/\/w{3}\.(facebook|linkedin)\.com\/(in\/)?[a-zA-Z0-9._-]+\/?$|^mailto:\w+"))
	
	related_facebook = []
	related_mail = []
	related_linkedin = []

	for link in links:
		
		href= link['href']

		if 'facebook' in href:
			if href not in related_facebook:
				related_facebook.append(href)

		if 'mailto' in href:
			mailto = href.split(':')
			if mailto[1] not in related_mail:
				related_mail.append(mailto[1])

		if 'linkedin' in href:
			if href not in related_linkedin:
				related_linkedin.append(href)

	websitelinks = {}

	if related_linkedin:
		websitelinks['linkedin'] = related_linkedin
	if related_facebook:
		websitelinks['facebook'] = related_facebook
	if related_mail:
		websitelinks['mail']= related_mail

	return websitelinks



