#takes a users input word and prints it out backwards

word = input("what word should be printed backwards?")
new = ""

for i in reversed(word): 
  new = str(new) + i

print(new)




