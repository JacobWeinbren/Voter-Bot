# -*- coding: utf-8 -*-
import csv, random

file = list(csv.DictReader(open("Voters.csv")))
las = {}
authorities = list(csv.DictReader(open("LA.csv")))
for authority in authorities:
	las[authority['PCON16CD']] = authority['PCON16NM']

countries = {
	1: '🏴󠁧󠁢󠁥󠁮󠁧󠁿',
	2: '🏴󠁧󠁢󠁳󠁣󠁴󠁿',
	3: '🏴󠁧󠁢󠁷󠁬󠁳󠁿'
}

religions = {
	1: '',
	2: '(CoE) ',
	3: 'Catholic ',
	4: '(CoS)',
	5: 'Methodist ',
	6: 'Baptist ',
	7: 'Protestant ',
	8: 'Protestant ',
	9: 'Protestant ',
	10: 'Jewish ',
	11: 'Hindu ',
	12: 'Muslim ',
	13: 'Sikh ',
	14: 'Buddhist ',
	15: 'Religious ',
	16: '',
	17: 'Orthodox ',
	18: 'Pentecostal ',
	19: 'Evangelical '
}

parties = {
	1: "Con",
	2: "Lab",
	3: "Lib Dem",
	4: "SNP",
	5: "PC",
	6: "UKIP",
	7: "Green",
	9: "Other"
}

media = {
	0: '📺',
	1: '🗞️',
	2: '📻',
	3: '💻',
	4: '🗣️'
}

papers = {
	1: 'Express',
	2: 'Mail',
	3: 'Mirror',
	4: 'Star',
	5: 'Sun',
	6: 'Telegraph',
	7: 'FT',
	8: 'Guardian',
	9: 'Independent',
	10: 'Times',
	11: 'Scotsman',
	12: 'Herald',
	13: 'Western',
	14: 'Local',	
	15: 'Local'	
}

issues_cat = {
	1: "health 🏥",
	2: "education 🏫",
	3: "the next election outcome 🗳️",
	4: "negative politics 😓",
	5: "partisan politics 🗯️",
	7: "societal divides 🇬🇧",
	8: "morals 🔱",
	9: "national identity 🇬🇧",
	10: "welfare 🏠",
	11: "terrorism 🚨",
	12: "immigration 🛃",
	13: "asylum seekers 🛃",
	14: "crime 🚓",
	15: "Europe 🇪🇺",
	16: "constitutional issues 📜",
	17: "international trade 🚢",
	18: "devolution 📜",
	19: "Scottish independence 🇬🇧",
	21: "foreign affairs 🎖️",
	22: "war / defence 🎖️",
	23: "war / defence 🎖️",
	26: "the wider economy 💷",
	27: "my economic standing 💷",
	28: "unemployment 📈",
	29: "taxation 📈",
	30: "the debt / deficit 📈",
	31: "inflation 📈",
	32: "living costs 📈",
	33: "poverty 📈",
	34: "austerity 📈",
	35: "inequality 📈",
	36: "housing 🏠",
	37: "social care 🏥",
	38: "pensions / ageing 🧓",
	39: "transport and infrastructure 🚅",
	40: "the environment 🌳",
	47: "the EU referendum 🇪🇺"
}

genders = {1: 'man', 2: 'woman'}
values = {}

with open("lines.txt", "w") as f:
	for number in range(len(file)):
		person = file[number]
		if int(person['education']) in [13, 14, 15, 16, 17, 18]:
			education = 'university-educated'
		else:
			education = 'non-university-educated'

		age = int(person['age'])
		try:
			religion = religions[int(person['profile_religion'])]
		except:
			religion = ''
		gender = genders[int(person['gender'])]
		country = countries[int(person['country'])]

		lr = float(person['leftRight'])
		if lr < 5:
			if lr < 2:
				lr = 'V Left Wing ⏪'
			else:
				lr = 'C Left ◀️'
		elif lr == 5:
			lr = 'Centre ⏸️'
		elif lr > 5:
			if lr >= 8:
				lr = 'V Right Wing ⏩'
			else:
				lr = 'C Right ▶️'
		else:
			lr = ''

		issues = []


		try:
			if int(person['socialCare']) in [4]:
				issues.append('Support private social care 💼')
			if int(person['socialCare']) in [5]:
				issues.append('❗Support private social care 💼')
			if int(person['socialCare']) in [2]:
				issues.append('Support public social care 🏛')
			if int(person['socialCare']) in [1]:
				issues.append('❗Support public social care 🏛')
		except:
			pass

		if country == '🏴󠁧󠁢󠁳󠁣󠁴󠁿':
			try:
				if int(person['satDemScot']) in [3]:
					issues.append('Satisified with Scottish Democracy 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
				if int(person['satDemScot']) in [4]:
					issues.append('❗Satisified with Scottish Democracy 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
				if int(person['satDemScot']) in [2]:
					issues.append('Dissatisfied with Scottish Democracy 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
				if int(person['satDemScot']) in [1]:
					issues.append('❗Dissatisfied with Scottish Democracy 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
				if int(person['scottishness']) in [3,4,5,6,7]:
					issues.append('Feel Strongly Scottish 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
			except:
				pass

		elif country == '🏴󠁧󠁢󠁷󠁬󠁳󠁿':
			try:
				if int(person['satDemWales']) in [3]:
					issues.append('Satisified with Welsh Democracy 🏴󠁧󠁢󠁷󠁬󠁳󠁿')
				if int(person['satDemWales']) in [4]:
					issues.append('❗Satisified with Welsh Democracy 🏴󠁧󠁢󠁷󠁬󠁳󠁿')
				if int(person['satDemWales']) in [2]:
					issues.append('Dissatisfied with Welsh Democracy 🏴󠁧󠁢󠁷󠁬󠁳󠁿')
				if int(person['satDemWales']) in [1]:
					issues.append('❗Dissatisfied with Welsh Democracy 🏴󠁧󠁢󠁷󠁬󠁳󠁿')
				if int(person['welshness']) in [3,4,5,6,7]:
					issues.append('Feel Strongly Welsh 🏴󠁧󠁢󠁷󠁬󠁳󠁿')
			except:
				pass

		else:
			try:
				if int(person['satDemUK']) in [3]:
					issues.append('Satisified with UK Democracy 🗳️')
				if int(person['satDemUK']) in [4]:
					issues.append('❗Satisified with UK Democracy 🗳️')
				if int(person['satDemUK']) in [2]:
					issues.append('Dissatisfied with UK Democracy 🗳️')
				if int(person['satDemUK']) in [1]:
					issues.append('❗Dissatisfied with UK Democracy 🗳️')
				if int(person['englishness']) in [3,4,5,6,7]:
					issues.append('Feel Strongly English 🏴󠁧󠁢󠁥󠁮󠁧󠁿')
			except:
				pass

		try:
			if int(person['handleEUNegotiate']) in [4]:
				issues.append('Satisified with Government Handling Brexit 🇪🇺')
			if int(person['handleEUNegotiate']) in [5]:
				issues.append('❗Satisified with Government Handling Brexit 🇪🇺')
			if int(person['handleEUNegotiate']) in [2]:
				issues.append('Dissatisfied with Government Handling Brexit 🇪🇺')
			if int(person['handleEUNegotiate']) in [1]:
				issues.append('❗Dissatisfied with Government Handling Brexit 🇪🇺')
		except:
			pass

		if country == '🏴󠁧󠁢󠁳󠁣󠁴󠁿':
			try:
				if int(person['scotReferendumIntention']) in [0]:
					issues.append('Oppose Scottish Indy 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
				if int(person['scotReferendumIntention']) in [1]:
					issues.append('Support Scottish Indy 🏴󠁧󠁢󠁳󠁣󠁴󠁿')
			except:
				pass
				
		try:
			if int(person['EUIntegrationSelf']) in [6, 7, 8]:
				issues.append('Oppose EU integration 🇪🇺')
			if int(person['EUIntegrationSelf']) in [9, 10]:
				issues.append('❗Oppose EU integration 🇪🇺')
			if int(person['EUIntegrationSelf']) in [2, 3, 4]:
				issues.append('Support EU integration 🇪🇺')
			if int(person['EUIntegrationSelf']) in [0, 1]:
				issues.append('❗Support EU integration 🇪🇺')
		except:
			pass

		try:
			if int(person['tuitionFeesTooFar']) in [4]:
				issues.append('Oppose Raising Tuition Fees 🎓')
			if int(person['tuitionFeesTooFar']) in [5]:
				issues.append('❗Oppose Raising Tuition Fees 🎓')
			if int(person['tuitionFeesTooFar']) in [2]:
				issues.append('Support Raising Tuition Fees 🎓')
			if int(person['tuitionFeesTooFar']) in [1]:
				issues.append('❗Support Raising Tuition Fees 🎓')
		except:
			pass

		try:
			if int(person['al2']) in [2]:
				issues.append('Oppose the death penalty ❌')
			if int(person['al2']) in [1]:
				issues.append('❗Oppose the death penalty ❌')
			if int(person['al2']) in [4]:
				issues.append('Support the death penalty ✔️')
			if int(person['al2']) in [5]:
				issues.append('❗Support the death penalty ✔️')
		except:
			pass

		try:
			if int(person['lr1']) in [4]:
				issues.append('Support wealth redistribution 💷')
			if int(person['lr1']) in [5]:
				issues.append('❗Support wealth redistribution 💷')
			if int(person['lr1']) in [2]:
				issues.append('Oppose wealth redistribution 💷')
			if int(person['lr1']) in [1]:
				issues.append('❗Oppose wealth redistribution 💷')
		except:
			pass

		try:
			if int(person['econGenRetro']) in [2]:
				issues.append('Economy is worse in last 12 months 📉')
			if int(person['econGenRetro']) in [1]:
				issues.append('❗Economy is worse in last 12 months 📉')
			if int(person['econGenRetro']) in [4]:
				issues.append('Economy is better in last 12 months 📈')
			if int(person['econGenRetro']) in [5]:
				issues.append('❗Economy is better in last 12 months 📈')
		except:
			pass

		try:
			if int(person['euPriorityBalance']) in [2,3]:
				issues.append('Brexit priority: Single Market access 🌐')
			if int(person['euPriorityBalance']) in [0,1]:
				issues.append('❗Brexit priority: Single Market access 🌐')
			if int(person['euPriorityBalance']) in [7,8]:
				issues.append('Brexit priority: Controlling immigration 🛃')
			if int(person['euPriorityBalance']) in [9,10]:
				issues.append('❗Brexit priority: Controlling immigration 🛃')
		except:
			pass

		try:
			if int(person['effectsEUFinance']) in [4]:
				issues.append('Brexit: Improves my financial position 📈')
			if int(person['effectsEUFinance']) in [5]:
				issues.append('❗Brexit: Improves my financial position 📈')
			if int(person['effectsEUFinance']) in [2]:
				issues.append('Brexit: Worsens my financial position 📉')
			if int(person['effectsEUFinance']) in [1]:
				issues.append('❗Brexit: Worsens my financial position 📉')
		except:
			pass

		try:
			if int(person['euLeaveVoice']) == 4:
				issues.append("Brexit: Improves Britain's influence 🇬🇧")
			if int(person['euLeaveVoice']) == 5:
				issues.append("❗Brexit: Improves Britain's influence 🇬🇧")
			if int(person['euLeaveVoice']) == 2:
				issues.append("Brexit: Reduces Britain's influence 🇬🇧")
			if int(person['euLeaveVoice']) == 1:
				issues.append("❗Brexit: Reduces Britain's influence 🇬🇧")
		except:
			pass

		try:
			if int(person['effectsEUNHS']) == 4:
				issues.append('Brexit: Improves the NHS 🏥')
			if int(person['effectsEUNHS']) == 5:
				issues.append('❗Brexit: Improves the NHS 🏥')
			if int(person['effectsEUNHS']) == 2:
				issues.append('Brexit: Worsens the NHS 🏥')
			if int(person['effectsEUNHS']) == 1:
				issues.append('❗Brexit: Worsens the NHS 🏥')
		except:
			pass

		try:
			if int(person['policeCuts']) == 4:
				issues.append('Police cuts have gone too far 🚓')
			if int(person['policeCuts']) == 5:
				issues.append('❗Police cuts have gone too far 🚓')
			if int(person['policeCuts']) == 2:
				issues.append('Police cuts have not gone far enough 🚓')
			if int(person['policeCuts']) == 1:
				issues.append('❗Police cuts have not gone far enough 🚓')
		except:
			pass

		try:
			if int(person['small_mii_cat']):
				issues.append("Britain's most important issue is " + issues_cat[int(person['mii_cat'])])
		except:
			pass


		try:
			sources = [int(person['infoSourceTV']), int(person['infoSourcePaper']), int(person['infoSourceRadio']), int(person['infoSourceInternet']), int(person['infoSourcePeople'])]
			sources = [x if x != 999 else 1 for x in sources]
			source = media[sources.index(max(sources))]
			if source == '🗞️' and int(person['profile_newspaper']) in papers.keys():
				source += " (" + papers[int(person['profile_newspaper'])] + ")"

			a = ["I'm a ", str(age), " year old " + religion + gender +", ", education, ". ", las[person['onscode']], " ", country + ". News ", source]
			
			if int(person['euRefVote']) == 1:
				c = lr + " I voted Leave in 2016"
			if int(person['euRefVote']) == 0:
				c = lr + " I voted Remain in 2016"
			if int(person['euRefVote']) == 2:
				c = lr + " I didn't vote in 2016"
			if int(person['euRefVote']) == 99:
				c = lr + " I didn't vote in 2016"
			
			turnout = int(person['profile_turnout_2017'])
			vote = int(person['profile_past_vote_2017'])
		
			if vote == 0 or turnout == 0 or vote == 9999:
				c += " and didn't vote in 2017"
			else:
				if vote in parties.keys() and turnout == 1:
					party = parties[vote]
			
			if party and "2017" not in c:
				if "didn't" in c:
					c += " and voted " + party + " in 2017"
				else:
					c += " and " + party + " in 2017"

			items = [1, 1]
			b = []
			for i in range(281):
				b.append('a')
			count = 0
			while len("".join(a))+len("".join(b))+len("".join(c)) + 4> 280 and count < 100:
				count += 1
				items = random.sample(issues, 3)
				b = "- " + items[0] + "\n" + "- " + items[1] + "\n" + "- " + items[2]

			if a and b and c:
				if len("".join(a))+len("".join(b))+len("".join(c)) + 4 < 280:
					f.write("".join(a) + "\n" + "".join(b) + "\n" + "".join(c) + "\n")
		except:
			pass