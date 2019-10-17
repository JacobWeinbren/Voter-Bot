# -*- coding: utf-8 -*-
from access import *

with open("lines.txt") as file:
	count = 17310
	lines = file.readlines()
	tweet = lines[count+0]+ "\n" + lines[count+1] + lines[count+2] + lines[count+3]+ "\n" + lines[count+4]
	tweet = tweet.decode('utf-8')
	status = api.update_status(tweet)
	print(status.text)
with open("secondcount", "w") as secondchange:
	secondchange.write("0")
