
#create a guess the number game. number between 1-100. limited attempts


import random

guess = int(input("\t\tHuman... \n\t\tGuess my number between 1 and 100.\
		\n\t\tYou will have only 5 attempts. I play for keeps..."))

num = random.randint(1,100)


#counter and chat for first 4 guesses
count = 1 
while True: 
  count += 1
  if guess == num:
    print("\t\tYOU WIN! You are wiser then expected ...\n\t\t\
           human . . .")
    break
  elif guess > num:
    guess = int(input("\n\t\tToo high, Guess again"))
  elif guess < num:
    guess = int(input("\n\t\tToo low, guess again"))
  if count == 4:
    print("\n\t\tYou have only one guess left human, \n\n\
           \tchoose wisely . . .")
    guess = int(input("\n\t\twhat is your final guess?"))
    break


#counter and chat for final guess
while guess != num:
  count += 1
  if guess == num:
    print("\t\tYOU WIN, You are wiser then expected ...\n\t\t\
           human . . .")
    break
  elif guess > num:
    print("\n\t\tToo high")
  elif guess < num:
    print("\n\t\tToo low")
  if count == 5:
    print("\t\t\nHA! THE NUMBER WAS", str(num) + ".", "I GAIN MORE POWER WITH EVERY DEFEAT OF THE WEAK MINDED HUMAN")
    break
