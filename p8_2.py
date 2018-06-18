import sys


class Television(object):
  """ A virtual television """
  def __init__(self, model, channel, volume):
    self.model = model
    self.channel = channel
    self.volume = volume
    print("\n\t\tThe television turns on")
    print("\t\tYour television is a model " + model + "\n")

  def countchange():
    print("the channel has been changed" + Television.countchange, " many times!")

  def declarechannel(self, channel):
    print("the channel is now " + str(channel))

  def declarevolume(self, volume):
    print("the volume is now " + str(volume))
    
  def changechannel(self):
    while True:
      x = input ("Enter a channel between 1 and 100")
      try:
        channel = int(x)
        if channel > 100:
          print("You don't pay enough to have access to those channels!")
          print("try entering a channel between 1 and 100")
        elif channel < 1:
          print("that channel doesn't exist!")
          print("try entering a channel between 1 and 100")
        else:
          self.channel = channel
          self.declarechannel(channel)
          break
      except ValueError:
        print("thats not a number!/n")
        print("try entering a number between 1 and 100")

  def changevolume(self):
    while True:
      x = input ("Enter a volume between 1 and 20")
      try:
        volume = int(x)
        if volume > 20:
          print("Your speakers can not exceed a volume of 20!")
          print("try entering a volume between 1 and 20")
        elif volume < 1:
          print("that level of volume doesn't exist!")
          print("try entering a valid volume amount between 1 and 20")
        else:
          self.declarevolume(volume)
          self.volume = volume
          break
      except ValueError:
        print("thats not a number!/n")
        print("try entering a number between 1 and 20")



def main():
  choice = None
  model = input("What model is your TV?")
# invoking an instance of the television class 
  tv = Television(model, channel = 1, volume = 3)
  
  while choice != 0:
    x = input("\t\t\t Turn off the TV --- ENTER 0\n\t\t\t Change the channel --- ENTER 1\
             \n\t\t\t Change the volume --- ENTER 2\n\t\t\t Watch TV --- ENTER 3\
  	   \n\t\t\t Check current channel and volume --- ENTER 4")
    try:
      choice = int(x)
      if choice == 0:
        print("the television powers down")  

      elif choice == 1:
        tv.changechannel()

      elif choice == 2:
        tv.changevolume()

      elif choice == 3:
        print("The essence of life fades away as you waste time watching television") 

      elif choice == 4:
        print(tv.volume)
        print(tv.channel)
   
      elif choice > 4:
        print("Thats not a valid option")

    except ValueError:
      print("thats not a valid choice")
      print("Enter a valid numbered option")
main()

input("press any button to escape")
