#create a program that prints a list of words in a random order

import random

words = ["frog", "cat", "mouse", "rat"]
output = []
position = 0

while words:
  position = random.randrange(len(words))
  output.append(words[position])
  del words[position]

print (output)
