#I edited the original program so that each question has it's own unique point reward
#program tracks players highscore in a seperate text file using the pickle function


from operator import itemgetter
import sys, pickle, shelve, os

global high_scores

def_highscores = [("vacant",0),("vacant",0),("vacant",0),("vacant",0),("vacant",0),("vacant",0),("vacant",0),("vacant",0),("vacant",0),("vacant",0)]

#ensures file exists, if not creates one
#makes sure file has something in it, if not put in the vacant markers
def setup_scores(filee):
  if os.path.isfile(filee) == False:
    with open(filee, "wb") as h:
      pickle.dump(def_highscores, h, protocol=pickle.HIGHEST_PROTOCOL)

  if os.path.getsize(filee) == 0:
    with open(filee, "wb") as h:
      pickle.dump(def_highscores, h, protocol=pickle.HIGHEST_PROTOCOL)

#open file and edit list
def save_score(name, new_score, filee):
  with open(filee, "rb") as h:
    high_scores = pickle.load(h)
    high_scores.append((name, new_score))
    high_scores = sorted(high_scores, key=itemgetter(1), reverse = True)[:9]
    return high_scores
    
def push_list(filee, the_list):
    with open(filee, "wb") as h:
      pickle.dump(the_list, h, protocol=pickle.HIGHEST_PROTOCOL)
    

def open_file(file_name, mode):
  """open a text file"""
  try:
    the_file = open(file_name, mode)
  except IOError: 
    print("I couldn't locate your file.")
    input("press enter to close")
    sys.exit()
  else:
    return the_file

def next_line(the_file):
  """Return next line from trivia file, formatted"""
  line = the_file.readline()
  line = line.replace("/", "\n")
  return line

def next_block(the_file):
  """Return the next block of data from the trivia file"""
  category = next_line(the_file)

  question = next_line(the_file)

  anwsers = []
  for i in range(4):
    anwsers.append(next_line(the_file))

  correct = next_line(the_file)

  points = next_line(the_file)
##  This if statement checks to see if there is an answer, if not it does not return a value  
  if correct:
    correct = correct[0]

  explanation = next_line(the_file)
  
  return category, question, anwsers, correct, explanation, points


#the title is the first line in the text file
def welcome(title):
  """Welcome the player to the game"""
  print("\t\tWelcome to The trivia challenge!")
  print("\t\t", title, "\n")

def main():
  high_scores = []
  trivia_file = open_file("game_map.txt", "r")
  title = next_line(trivia_file)
  welcome(title)
  score = 0

  category, question, anwsers, correct, explanation, points = next_block(trivia_file)
  while category:
    #ask question
    print(category)
    print(question)
    for i in range(4):
      print("\t", i+1, "-", anwsers[i])

    #get anwser
    anwser = input("What's your anwser?")
    if anwser == correct:
      print("\nRight!", end=" ")
      score += int(points)
    else:
      print("\nWrong!", end=" ")
    print(explanation)
    print("Score:", score, "\n\n")

    category, question, anwsers, correct, explanation, points = next_block(trivia_file)

  trivia_file.close()
  
  print("that was the last question!")
  print("Your score is ", score)

  setup_scores("high_scores.dat")
  high_scores = save_score(input("What is your name?"), score, "high_scores.dat")
  push_list("high_scores.dat", high_scores)

  with open("high_scores.dat","rb") as f:
    the_scores = pickle.load(f)
    #the_scores.reverse()
    print(the_scores)

#Purpose - if you need to use a function from this file, you can import it
#and not worry about executing the main function. Because the variable __name__ will not equal "__main__" in that case
if __name__ == "__main__":
  
  main()
