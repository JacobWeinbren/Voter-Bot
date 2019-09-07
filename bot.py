# -*- coding: utf-8 -*-
from access import *

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