#guess the random word, computer indicates the number of letters in the word
#i
import random

WORDS = ("apple", "orange", "peach", "pear")
words = WORDS

print("\tGuess the word, I will only reveal the number of letters in each word")
input("\n\tAre you ready?")


while True:
  mark = random.randrange(len(words))	
  choice = words[mark]
  anwser = choice
  var = choice
  words = words[:mark] + words[(mark+1):]


  counter = 0

  while anwser:
    position = random.randrange(len(anwser))
    counter += 1
    anwser = anwser[:position] + anwser[(position+1):]


  print("\n\tYour word is comprised of", counter, "letters")
  
  count = 0

  while True: 
    count += 1
    guess = input("\n\tGuess a letter in the hidden word")

    if guess in var:
      print("\n\tYes")

    else:
      print("\n\tNo")

    if count == 5:
      print("\n\tYou have now had 5 guesses")
      response = input("\tWhat is the secret word?")
      break


  if response == var:
    print("\n\tYou've guessed right!")
    remain = input("\tContinue playing -press  y to CONTINUE, - n to END").lower()

  else:
    print("\n\tYou've guessed wrong!")
    print("\tThe secret word your failed to identify was", var)
    remain = input("\tContinue playing - press  y to CONTINUE, n to END").lower()

  if remain == "y":
    continue

  else remain == "n":
    print("\n\tThanks for playing!")
    break
 

