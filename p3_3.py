
#create a guess the number game. number between 1-100. limited attempts


import random

guess = int(input("\t\tHuman... \n\t\tGuess my number between 1 and 100.\
		\n\t\tYou will have only 5 attempts. I play for keeps..."))

num = random.randint(1,100)



count = 0
while True: 
  if guess == num:
    print("\t\tYou are wiser then expected ...\n\t\t\
           human . . .")
  
  elif guess > num:
    count += 1
    guess = int(input("\n\t\tToo high, Guess again"))

  elif guess < num:
    count += 1
    guess = int(input("\n\t\tToo low, guess again"))

  if count == 4:
    print("\n\t\tYou have only one guess left human, \n\n\
           \tI knew you were weak minded")

  if count == 5:
    print("\t\t\nHA! THE NUMBER WAS", str(num) + ".", "I GAIN MORE POWERFUL WITH EVERY DEFEAT OF THE WEAK MINDED HUMAN")
    break
