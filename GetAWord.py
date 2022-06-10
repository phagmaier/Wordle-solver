def getWord(words, greenLetters, yellowLetters, badLetters):
	possible_words = []
	for i in words:
		good = True
		for l in badLetters:
			if l in i:
				good = False
				continue
		for x in greenLetters:
			if x not in i:
				good = False
				continue
			if isinstance(greenLetters[x], list) == True:
				for y in greenLetters[x]:
					if i[y] != x:
						good = False
						continue
			else:
				if i[greenLetters[x]] != x:
					good = False
					continue
		for r in yellowLetters:
			if r not in i:
				good = False
				continue
			if isinstance(yellowLetters[r], list) == True:
				for g in yellowLetters[r]:
					if i[g] == r:
						good = False
						continue
			else:
				if i[yellowLetters[r]] == r:
					good = False
					continue
		if good == True:
			possible_words.append(i)

	letterDic = {}
	for i in possible_words:
		for x in i:
			if x in letterDic:
				letterDic[x] += 1
			else:
				letterDic[x] = 1

	#key_list = list(my_dict.keys())
	wordRankings = {}
	for i in possible_words:
		wordRankings[i] = 0
		letters = []
		for x in i:
			if x not in letters:
				letters.append(x)
				wordRankings[i] += letterDic[x]

	topValue = wordRankings[possible_words[0]]
	wordRec = possible_words[0]
	for i in possible_words:
		if wordRankings[i] > topValue:
			wordRec = i
			topValue = wordRankings[i]

	return wordRec, possible_words

