import random
import sys

input("\n\t\tcare to play a game? - press any button to contine")
print("\n\t\tI challenge you to compete against me in a game of skill\
	\n\t\tWhoever can guess the secret number between 1 - 100 wins")

input("\t\tdo you accept? press any button to accept")

print("\n\t\tWe begin - the secret number has been chosen, not even I know it's value!")

num = random.randrange(100)+1
human = int(input("\n\t\twhat is your first guess?"))
robot = 0
count = 1 


while count != 5:
  count += 1
  if robot ==num:
    print("\n\t\tYou lose, I win")

  if robot > num:
    print("\t\tI guess the number " + str(robot))
    print("\t\tI've guessed too high")
    human = int(input("\t\twhat is your next guess human?"))

  if robot < num and count > 2:
    print("\t\tI guess the number " + str(robot))
    print("\t\tI've guessed too low")
    human = int(input("\t\tWhat is your next guess human?"))

  if human ==num:
    print("\n\t\tSomehow...you win\n congratulations\
		on your victory")
    sys.exit()

  elif human > num:
    print("\n\t\tToo high")
    if count != 5:
      print("\n\t\tMy turn")
      robot = random.randrange(100)+1


  elif human < num:
    print("\n\t\tToo low")
    if count != 5:
      print("\n\t\tMy turn")
      robot = random.randrange(100)+1

  if count == 5:
    human = int(input("\t\twhat is your final guess?"))

robot = 0

while count != 7:
  count += 1
  if robot ==num:
    print("\n\t\tYou lose, I win")

  if robot > num:
    print("\n\t\tI've guessed too high, How could I not win? The match is a DRAW")
    break

  if robot < num and robot > 0: 
    print("\n\t\tI've guessed too low, How could I not win?. The match is A DRAW")
    break

  if human == num:
    print("\n\t\tCongratulations on your victory")
    break

  elif human > num:
    print("\n\t\tToo high")
    robot = random.randrange(100)+1
    print("\n\t\tMy final guess is " + str(robot))
    
  elif human < num:
    print("\n\t\tToo low")
    robot = random.randrange(100)+1
    print("my final guess is " + str(robot)) 
















