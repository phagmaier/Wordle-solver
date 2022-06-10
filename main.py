import requests
from bs4 import BeautifulSoup
from GetAWord import getWord
# "https://medium.com/@owenyin/here-lies-wordle-2021-2027-full-answer-list-52017ee99e86"
def getPage(url):
  res = requests.get(url)
  #print(res.status_code)
  if res.status_code == 200:
    return res.content 


def getHtmlPage(fileName):

  with open(fileName) as f:
    data = f.read()

  return data


def getWords(html):
  soup = BeautifulSoup(html, 'html.parser')

  paragraphs = soup.find_all('p')

  results = []
  
  for par in paragraphs:
    if 'CIGAR' in par.text:
      words = str(par)
      words = words[:-4]
      words = words.split("<br/>")
      #print(words)
      parts = words[0].split('>')
      words[0] = parts[-1]
      for word in words:
        #print(word[-5:])
        results.append(word[-5:])

  results = list(set(results))
  return results

if __name__=='__main__':
  #words, greenLetters, yellowLetters, badLetters
  html = getHtmlPage("mediumPage.html")
  words = getWords(html)
  words = sorted(words)
  badLetters = []
  count = 0
  results = None
  #need to make all letter suppercase
  while count < 5:
    badLetters = []
    greenLetters = {}
    yellowLetters = {}
    anotherLetter = None
    aLetter = None
    badLetter = None
    while aLetter != 'done':
      aLetter = input("Enter one green letter. Enter done when finished: ")
      if aLetter != 'done':
        aLetter = aLetter.upper()
        position = input("Enter the position of the letter from 0-4: ")
        if aLetter in greenLetters:
          if isinstance(greenLetters[aLetter], list) == True:
            aList = [m for m in greenLetters[aLetter]]
            aList.append(int(position))
          else:
            aList = []
            aList.append(greenLetters[aLetter])
            aList.append(int(position))
          greenLetters[aLetter] = aList
        else:
          greenLetters[aLetter] = int(position)
    while anotherLetter != 'done':
      anotherLetter = input("Enter one yellow letter. enter done when finished: ") 
      if anotherLetter != 'done':
        anotherLetter = anotherLetter.upper()
        position = input("Enter the position of the letter from 0-4: ")
        if anotherLetter in yellowLetters:
          if isinstance(yellowLetters[anotherLetter], list) == True:
            aList = [m for m in yellowLetters[anotherLetter]] 
            aList.append(int(position))
            yellowLetters[anotherLetter] = aList
          else:
            aList = []
            aList.append(yellowLetters[anotherLetter])
            aList.append(int(position))
            yellowLetters[anotherLetter] = aList
        else:
          yellowLetters[anotherLetter] = int(position)
    while badLetter != 'done':
      badLetter = input("Enter one grey letter: ")
      if badLetter != 'done':
        badLetter = badLetter.upper()
        badLetters.append(badLetter)
      else:
        count += 1
        if results == None:
          aResult = getWord(words, greenLetters, yellowLetters, badLetters)
          results = aResult[1]
        else:
          aResult = getWord(results, greenLetters, yellowLetters, badLetters)
          results = aResult[1]

        print("The word we recomend is: " + aResult[0])