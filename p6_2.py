import random


def ask_number(question, low, high, step = 1):
  """Ask for a number within a range."""
  response = None
  while response not in range(low, high, step):
    response = int(input(question))
    return response



guess = ask_number("Guess my number betweeen 1 and 100", 1, 100)

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
    guess = ask_number("\n\t\tToo high, Guess again",1,100)
  elif guess < num:
    guess = ask_number("\n\t\tToo low, guess again",1,100)
  if count == 4:
    print("\n\t\tYou have only one guess left human, \n\n\
           \tchoose wisely . . .")
    guess = ask_number("\n\t\twhat is your final guess?",1,100)
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
