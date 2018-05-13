#word jumble game
#user is given random word, scrambled, has to guess the word

import random
import sys

WORDS = ("cowboy","donkey","chicken", "piglet")
words= WORDS
HINTS = ("mancalf","Mary rode to Bethlehem","cuck with an l","oinksmall")
hints = HINTS

print("Try to guess the jumbled word")
input("Press ENTER to continue")

count = 0
score = 0

while score != 100:
  if count != 0:
    check = input("press ENTER to continue playing, otherwise type EXIT to quit").lower()
    if check == "exit":
      sys.exit()
  
  count +=1

  jumble =""
  mark = random.randrange(len(words))
  select = words[mark]
  words = words[:mark] + words[(mark+1):]
  hints = hints[:mark] + hints[(mark+1):]

  while select:
    position = random.randrange(len(select))
    jumble += select[position]
    select = select[:position] + select[(position+1):]
    

  while True:
    print (jumble)
    hint = str((input("do you require a hint? - enter  y or n").lower()))
    if hint == "y":
      print("Your hint is this - " + HINTS[mark])
      input("Press ENTER to continue")
      break
    elif hint == "n":
      print("A bold move!")
      hint = False
      break
    else:
      print("that was not an expected response")
      print("try again")

  guess = str(input("what is your guess?"))

  if guess == WORDS[mark]:
    print("congratulations! your guess is correct")
    if hint == False:
      score += 10
      print("you are awarded 10 points")
      print("your new overall score is " + str(score))
    else:
      score += 5
      print("you are awarded 5 points")
      print("your new overall score is " + str(score))

  else:
    print("sorry, that's incorrect")
    print("you lose 10 points")
    score -= 10








