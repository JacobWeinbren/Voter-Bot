# -*- coding: utf-8 -*-
import twitter
api = twitter.Api(consumer_key='ZxOgNGdQ9jqvKndvnQIRk4XFe',
consumer_secret='TbOKCkoTkwuZtWOUEQ0x63H4tiOeUuCHdsbUBLAURRbJcXWpEj',
access_token_key='1140749728465989632-jXZitIRrtoriaFlH2QuUO118QndcPA',
access_token_secret='8Y7JuvulrB5lxqAER2P8xzTF8jBUjREkHDdHKK01pqotB')

with open("secondcount", "r") as second:
	count = int(second.readlines()[0])
	if count == 0:
		print "skipping"
		with open("secondcount", "w") as secondchange:
			secondchange.write("1")
	elif count == 1:
		with open("count", "r") as f:
			count = int(f.readlines()[0])
			with open("lines.txt") as file:
				lines = file.readlines()
				tweet = lines[count+0]+ "\n" + lines[count+1] + lines[count+2] + lines[count+3]+ "\n" + lines[count+4]
				tweet = tweet.decode('utf-8')
				status = api.PostUpdate(tweet)
				print(status.text)
			with open("secondcount", "w") as secondchange:
				secondchange.write("0")
				
		with open("count", "w") as f:
			f.write(str(count+1 * 5))