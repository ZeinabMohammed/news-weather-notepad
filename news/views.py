from django.shortcuts import render, redirect
import requests
requests.packages.urllib3.disable_warnings()
from datetime import timedelta, timezone, datetime
from bs4 import BeautifulSoup
from news.models import Headline,UserProfile
def scrape(request):
	# user_p = UserProfile.objects.filter(user=request.user)
	# user_p.last_scrape = datetime.now(timezone.utc)
	# user_p.save()
	session= requests.session()
	session.headers={"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.108 Safari/537.36"}
	URL = 'https://www.youm7.com/'
	content = session.get(URL, verify=False).content
	soup=BeautifulSoup(content, "html.parser")
	posts= soup.find_all('div', {'class':'newsInfo'})
	titles = [i.text for i in posts]
	# print(titles)
	# titles=(i for i in posts)
	# print(titles)
	# print(len(posts))
	# for i in posts:
	# 	title=i.text


	# 	print(title)
	# 	image=i.find('img')
	# 	link=i.find('a')
	
		# new_headline = Headline()
		# new_headline.title = title
		# new_headline.url = link
		# new_headline.image= image
	# headlines=Headline.objects.all().order_by('-id')[ :10]
	return render(request,'news.html', {'posts':posts,'titles':titles})




