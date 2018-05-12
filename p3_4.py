import random
import sys

input("\n\t\tCare to play a game? - Press ENTER to continue")
print("\n\t\tI challenge you to compete against me in a game of skill\
	\n\t\tWhoever can guess the secret number between 1 - 100 wins")

input("\t\tDo you accept? - Press ENTER to accept")

print("\n\t\tWe begin - the secret number has been chosen, not even I\n\t\tknow it's value!")

num = random.randrange(100)+1
human = int(input("\n\t\tWhat is your first guess?"))
robot = 0
count = 1 

#executes guesses 1-4
while count != 6:
  count += 1
  if robot ==num:
    print("\n\t\tYou lose, I win")

  if robot > num and count >2:
    print("\t\tI guess the number " + str(robot))
    print("\t\tI've guessed too high")
    if count !=6:
      human = int(input("\t\tWhat is your next guess human?"))

  if robot < num and count >2:
    print("\t\tI guess the number " + str(robot))
    print("\t\tI've guessed too low!")
    if count !=6: 
      human = int(input("\t\tWhat is your next guess human?"))

  if human ==num:
    print("\n\t\tSomehow...you won\n\t\t congratulations on your victory")
    sys.exit()

  elif human > num and count !=6:
    print("\n\t\tToo high!")
    print("\n\t\tMy turn")
    robot = random.randint(1,human)

  elif human < num and count !=6:
    print("\n\t\tToo low!")
    print("\n\t\tMy turn")
    robot = random.randint(human,100)

  if count == 6:
    human = int(input("\t\tWhat is your final guess?"))

robot = 0

#executes final guesses
while count != 8:
  count += 1
  if robot == num:
    print("\n\t\tYou lose, I win!")

  if robot > num:
    print("\t\tIve guessed too high!")
    print("\n\t\tThe secret number is "+ str(num) + "! How could I not win? The match is a DRAW")
    break

  if robot < num and robot > 0: 
    print("\t\tI've guessed too low!")
    print("\n\t\tThe secret number is " + str(num) + "! How could I not win? The match is a DRAW")
    break

  if human == num:
    print("\n\t\tCongratulations on your victory...")
    break

  elif human > num:
    print("\n\t\tToo high!")
    robot = random.randint(1,human)
    print("\n\t\tMy final guess is " + str(robot))
    
  elif human < num:
    print("\n\t\tToo low")
    robot = random.randint(human,100)
    print("\t\tMy final guess is " + str(robot)) 
















