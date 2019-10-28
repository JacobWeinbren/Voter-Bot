from access import *
import csv
import json

def get_all_tweets(screen_name):	
	#initialize a list to hold all the tweepy Tweets
	alltweets = []	
	
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	
	#save most recent tweets
	alltweets.extend(new_tweets)
	
	#save the id of the oldest tweet less one
	oldest = alltweets[-1].id - 1
	
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		
		#save most recent tweets
		alltweets.extend(new_tweets)
		
		#update the id of the oldest tweet less one
		oldest = alltweets[-1].id - 1
		
		print "...%s tweets downloaded so far" % (len(alltweets))
	
	#transform the tweepy tweets into a 2D array that will populate the csv	
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]
	
	#write the csv	
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	pass


file = list(csv.DictReader(open("VoterBritish_tweets.csv")))
voters = []
for tweet in file:
	text = tweet['text']
	text = text.replace('.', ',')
	text = text.split(',')
	if ' university-educated' in text:
		uni = 'university-educated'
	if ' non-university-educated' in text:
		uni = 'non-university-educated'
	start = text[0]
	age = 0
	try:
		age = int(start[6:8])
	except:
		pass
	if age > 10:
		items = start.split(' ')
		gender = items[-1]
		if items[-2] != 'old':
			religion = items[-2]
		else:
			if items[-2] == "Religious":
				religion = 'religious'
			else:
				religion = 'irreligious'
		if text[2][1:] != 'university-educated' and text[2][1:] != 'non-university-educated':
			loc = " ".join(text[2][1:].split(' ')[:-1])
		voters.append({
			'uni': uni,
			'loc': loc,
			'age': age,
			'gender': gender,
			'religion': religion
			})

with open('results.txt', 'w') as file:
	json.dump(voters,file)

for voter in voters:
	print voter['age']