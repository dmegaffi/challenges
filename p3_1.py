import random

fortune = random.randrange(4)

if fortune == 1:
    print("you smell like cheese, noone likes you")

elif fortune == 2:
    print("you smell like roses, everyone likes you")

elif fortune == 3:
    print("I see a prosperous future for you and your family")

elif fortune == 0:
    print("keep making good sacrifices, it is working!")

else:
    print("wow you are very fortunate to have such misfortune!")
