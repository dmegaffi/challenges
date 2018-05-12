#Write a program that counts for the user. 
#User picks the starting number, ending number, 
#and the amount by which to count.

input("Can I help you count? - Press ENTER to continue")
beg = int(input("What number should I start at?"))
end = int(input("Which number should I end at?")) + 1
inc = int(input("By which number should we increment by?"))


for i in range(beg, end, inc):
  print (i, end = " ")






