#character creator program where user has to assign 30 points amongst 4 attributes
#Some part os this code are repetitive and could likely be shortened with functions
#I am restricting myself to only using material taught so far in the book, functions have
#not yet been covered
import sys


name = input("\n\t\tEnter your characters name")

pools = {"\n\t\tstrength":0, "health":0, "wisdom":0, "dexterity":0}
points = 30
mark = False
count = 0

while True:
  count += 1
  while count >1 and mark == False:
    var = input("\n\t\tWould you like to continue to edit your characters attributes? - enter Y or N").lower()
    if var == "y":
      break
    elif var == "n":
      print("\n\t\tYour character:", name, "has the following attributes:\n", pools)
      print("\t\tGoodbye")
      sys.exit() 
    else:
      print("\n\t\tSorry I didn't understand that")
      continue

  print("\n\t\tYou have ", points, "remaining to be assigned")
  print("\t\tYou can add or take away points from any attribute")
  print("\t\tYour current skills are as follows, . . . \n\n", pools)
  print("""
              \n\n\t\t\tSTRENGTH ---------- ENTER 1
	      \t\tHEALTH ------------ ENTER 2
	      \t\tWISDOM ------------ ENTER 3
	      \t\tDEXTERITY --------- ENTER 4\n """)

  att = int(input("\n\t\tWhich attribute do you select?"))


  if att == 1:
    way = input("\t\tAre you increasing or decreasing the attribute pool?\n\t\tEnter UP or DOWN").upper()
    if way == "UP":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > points:
        print("\n\t\tsorry you do not have enough points to do that!")
      else:	
        pools["strength"] += movem
        points -= movem
        print("\n\t\tYou have added ", movem, " points to the attribute: strength")
    elif way == "DOWN":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > pools["strength"]:
        print("\n\t\tsorry you do not have enough points to do that!")
      else:
        pools["strength"] -= movem
        points += movem
        print("\n\t\tYou have removed ", movem, " points from the strength attribute")
        print("\t\tYou now have", pools["strength"], "points remaining in strength attribute.")
    else:
      print("\n\t\tsorry I didnt understand that response")
  
  elif att == 2:
    way = input("\t\tAre you increasing or decreasing the attribute pool?\n\t\tEnter UP or DOWN").upper()
    if way == "UP":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > points:
        print("\n\t\tsorry you do not have enough points to do that!")
      else:
        pools["health"] += movem
        points -= movem
        print("\n\t\tYou have added ", movem, " points to the attribute: health")
    elif way == "DOWN":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > pools["health"]:
        print("\n\t\tsorry you do not have enough points to do that!")
      else:
        pools["health"] -= movem
        points += movem
        print("\n\t\tYou have removed ", movem, " points from the health attribute")
        print("\t\tYou now have", pools["health"], "points remaining in health attribute.")
    else:
      print("\n\t\tsorry I didnt understand that response")

  elif att == 3:
    way = input("\t\tAre you increasing or decreasing the attribute pool?\n\t\tEnter UP or DOWN").upper()
    if  way == "UP":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > points:
        print("\n\tsorry you do not have enough points to do that!")
      else:
        pools["wisdom"] += movem
        points -= movem
        print("\n\t\tYou have added ", movem, " points to the attribute: wisdom")

    elif way == "DOWN":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > pools["wisdom"]:
        print("\n\t\tsorry you do not have enough points to do that!")
      
      else:
        pools["wisdom"] -= movem
        points += movem
        print("\n\t\tYou have removed ", movem, " points from the wisdom attribute")
        print("\t\tYou now have", pools["wisdom"], "points remaining in wisdom attribute.")
    else:
      print("\n\t\tsorry I didnt understand that response")

  elif att == 4:
    way = input("\t\tAre you increasing or decreasing the attribute pool?\n\t\tEnter UP or DOWN").upper()
    if way == "UP":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > points:
        print("\n\t\tsorry you do not have enough points to do that!")
      else:
        pools["dexterity"] += movem
        points -= movem
        print("\n\t\tYou have added ", movem, " points to the attribute: dexterity")
    elif way == "DOWN":
      movem = int(input("\n\t\tBy how many point?"))
      if movem > pools["dexterity"]:
        print("\n\t\tsorry you do not have enough points to do that!")
      else:
        pools["dexterity"] -= movem
        points += movem
        print("\n\t\tYou have removed ", movem, " points from the dexterity attribute")
        print("\t\tYou now have", pools["dexterity"], "points remaining in dexterity attribute.")
    else:
      print("\n\t\tsorry I didnt understand that response")




  if points == 0:
    mark = False
    print("\n\t\tYou have assigned all of your points!")
    exit = input("\n\t\tWould you like to exit? - enter Y or N")
    if exit == "y":
      print("\n\t\tYour character:", name, "has the following attributes:\n", pools)
      print("\t\tGoodBye!")
      break
    elif exit == "n":
      print("\n\t\tyou've chosen to continue editing your attribute distribution.")
      mark = True








