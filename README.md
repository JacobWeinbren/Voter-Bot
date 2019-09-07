# Voter-Bot

So a brief Q&A. I'm a student so the code is a bit messy, but I've broken it up.

**Where is the data from?**<br>
[Wave 13](https://www.britishelectionstudy.com/data-object/wave-13-of-the-2014-2018-british-election-study-internet-panel/) of the BES Study. It's in effect survey data weighted to the post 2017 election. After weighing, it was exported into a giant (relative to GitHub file standards) csv file called Voters.csv. Headers have all the variable names and then each voter has the responses. On the BES website, with the SPSS file, there's the full list of survey questions & variables. 

**How do you make the tweets?**<br>
The python program main.py recursively goes through each of the voters and in order just replaces variable values for prepared pieces of text. LA.csv is just a reference to convert codes to constituencies. The stuff it collects is around political views, demographics etc. The issues weren't picked with a clearly stated agenda at the time, just as salient/divisive questions. At the end, it goes through random issues until it finds a tweet under 280 characters. It's all put in a giant file called lines.

**How do you do the tweeting?**<br>
bot.py does the tweeting. And for API reasons, access.py just uses my key to do the tweeting but it's git-ignored. It's done from a pythonanywhere.com bot every hour.

**Why the emojis?**<br>
I thought it would look nicer.

**What should I do now?**<br>
Follow Chris and Dan, they're good people.
