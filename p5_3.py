p_dict = {"John jr.":"John S.", "Pat jr.":"Pat S.", "Fred jr.":"Fred S.", "Fran jr.":"Fran S."}
choice = 0 

import sys
import itertools
while True:
#creating a list of both gens 
  gen2 = []
  for x in p_dict:
    gen2.append(x)  
  var = p_dict.values()
  
  gen1 =[]
  for x in var:
    gen1.append(x)

  print(gen1)
  print(gen2)
  print(p_dict)

  print("""

          \n\n\t\t\tADD A PAIR------ENTER 1
          \t\tEDIT PAIR-------ENTER 2
          \t\tDELETE PAIR-----ENTER 3
          \t\tEXIT PROGRAN----ENTER 4
""")

  choice =int(input("\n\t\tWhat is your selection?"))

  if choice ==2:
    print("""                     
          \n\n\t\tEDIT GEN1 NAME-----ENTER 1
      \n\t\tEDIT GEN2 NAME---ENTER 2
      """)

    select = int(input("\n\t\tWhat is your selection?"))
    while True:
      mark = False
      count = -1
      if select == 1:
          print(gen1)
          who = input("Enter the first name of the person you would like to replace/edit.").title()
          for x in gen1:
            count += 1  
            if who in x:
              new = input("Enter the new name").title()
              var = gen2[count]
              gen1.remove(x)
              gen1.append(new)
              p_dict[var] = new
              mark = True
              break
          if mark == False:
            print("sorry that was not an expected response")
          else:
            print("Your changes are complete")
            break

      elif select == 2:
        print(gen2)
        who = input("Enter the first name of the person you would like to replace/edit.").title()
        for x in gen2:
          if who in x:
            new = input("Enter the new name:").title()
            p_dict[new] = p_dict.pop(x)
            gen2.remove(x)
            gen2.append(new)
            break
        break

  elif choice == 1:
    a = input("Enter the gen1 name you would add").title()
    gen1.append(a)
    b = input("Enter the gen2 name you would add").title()
    gen2.append(b)
    for (a, b) in zip(gen1, gen2):
      p_dict[b] = a
    print("Your entry has been a success")
    print(p_dict) 


  elif choice ==3:
    while True:
      print(p_dict)
      print(gen2)
      who = input("Enter the gen2 name of the pair you would delete").title()
      for x in gen2:
        if who in x:
          cat = x
          confirm = input("is this the pair you wanted? - y/n").lower()
          position = gen2.index(cat)
          if confirm == "y":
            del p_dict[cat]
            del gen2[position]
            del gen1[position]
            break
          if confirm == "n":
            break
      break

  elif choice ==4:
    print("Goodbye")
    sys.exit()

  else:
    print("sorry that was not an expected respnse")
