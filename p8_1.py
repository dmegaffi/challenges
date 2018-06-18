# Critter Caretaker
# A virtual pet to care for
#  The challenge was to improve the original program by allowing the user to specify how much food or
#  play time to spend on their critter
#my first challenge with classes

class Critter(object):
    """A virtual pet"""
    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name.title()
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    def __str__(self):
        return("hunger level is " + str(self.hunger) + \
               "\nboredom level is " + str(self.boredom))

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "happy"
        elif 5 <= unhappiness <= 10:
            m = "okay"
        elif 11 <= unhappiness <= 15:
            m = "frustrated"
        else:
            m = "mad"
        return m
    
    def talk(self):
        print("I'm", self.name, "and I feel", self.mood, "now.\n")
        self.__pass_time()
    
    def eat(self):
        while True:
          x = input("How much food would you like to feed " + self.name + ". Enter 1-9")
          try:
            food = int(x)
            if food > 9:
              print("woah thats too much food /n Try again")
            elif food < 0:
              print("woah thats not enough food for a meal /n Try again")
            else: 
              print("You fed " + self.name + " " +  str(food) + " units of food. " + self.name + " says 'Thank you!'")
              break
          except ValueError:
            print("thats not a number!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        while True:
          x = input("How many hours of play would you like to spend? Enter 1-9")
          try:
            fun = int(x)
            if fun > 9:
              print("woah thats too many hours! /n Try again")
            elif fun < 0:
              print("woah thats not enough time for a play session! /n Try again")
            else: 
              print("You played with " + self.name + " for " +  str(fun) + " many hours. " + self.name + " says 'Thank you!'")
              break
          except ValueError:
            print("thats not a number!")    
        print("Wheee!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    crit_name = input("What do you want to name your critter?: ")
    crit = Critter(crit_name)

    choice = None  
    while choice != "0":
        print \
        ("""
        Critter Caretaker
    
        0 - Quit
        1 - Listen to your critter
        2 - Feed your critter
        3 - Play with your critter
        """)
    
        choice = input("Choice: ")
        print()

        # exit
        if choice == "0":
            print("Good-bye.")

        # listen to your critter
        elif choice == "1":
            crit.talk()
        
        # feed your critter
        elif choice == "2":
            crit.eat()
         
        # play with your critter
        elif choice == "3":
            crit.play()

        #printing string representation of object
        elif choice == "4":
            print(crit)

        # some unknown choice
        else:
            print("\nSorry, but", choice, "isn't a valid choice.")

main()
("\n\nPress the enter key to exit.") 
