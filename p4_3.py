#word jumble game
#user is given random word, scrambled, has to guess the word
#must have a score feature, where player is penalized for accepting a hint

import random
import sys

WORDS = ("cowboy","donkey","chicken", "piglet")
words= WORDS
HINTS = ("mancalf","Mary rode to Bethlehem","cuck w/o an l","oinksmall")
hints = HINTS

print("\n\tTry to guess the jumbled word")
input("\n\tPress ENTER to continue")

count = 0
score = 0
last = False

while count !=4:
  if count == 3:
     print("\n\tThis is the final jumble - PREPARE YO\'SELF")
     last = True	

  if count !=0:
    check = input("\n\tPress ENTER to continue playing,  otherwise type EXIT to quit").lower()
    if check == "exit":
      sys.exit()
  
  count +=1

  jumble ="\t"
  mark = random.randrange(len(words))
  select = words[mark]
  
  #had to create var to hold value as their counterpart will be destroyed
  anwser = select
  hinter = hints[mark]
  
  words = words[:mark] + words[(mark+1):]
  hints = hints[:mark] + hints[(mark+1):]

  while select:
    position = random.randrange(len(select))
    jumble += select[position]
    select = select[:position] + select[(position+1):]
    

  while True:
    print ("\n" + jumble)
    hint = str((input("\n\tDo you require a hint? - enter  y or n").lower()))
    if hint == "y":
      print("\tYour hint is this - " + hinter)
      input("\n\tPress ENTER to continue")
      break
    elif hint == "n":
      print("\n\tA bold move!")
      hint = False
      break
    else:
      print("\n\tThat was not an expected response")
      print("\tTry again")

  guess = str(input("\tWhat is your guess?"))

  if guess == anwser:
    print("\n\tCongratulations! your guess is correct")
    if hint == False:
      score += 10
      print("\tYou are awarded 10 points")
      print("\tYour new overall score is " + str(score))
    else:
      score += 5
      print("\tYou are awarded 5 points")
      print("\tYour new overall score is " + str(score))

  else:
    score -= 10
    print("\n\tSorry, that's incorrect")
    print("\tYou lose 10 points")
    print("\tYour new overall score is " + str(score))

  if last == True:
    print("\n\tThanks for playing!")







