#heads and tails game. flip heads and tails 100 times
import random

tails = 0
heads = 0
count = 100

while count != 0:
  count -= 1
  flip = random.randrange(2)
  if flip == 0:
    heads += 1
  else:
    tails += 1

print ("tails was chosen", tails, "times")
print ("heads was chosen", heads, "times")
