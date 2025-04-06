#Fortune Cookie is a small cookie wafer with a piece of paper inside, called a “fortune”, which is usually a Chinese phrase with translation and a list of lucky numbers. They are served in restaurants in the U.S. and Canada.

import random

def fortune():
  x=random.randint(1,8)
  if x==1:
    print("Don't pursue happiness – create it.")
  elif x==2:
    print("All things are difficult before they are easy.")
  elif x==3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif x==4:
    print("Someone in your life needs a letter from you.")
  elif x==5:
    print("Don't just think. Act!")
  elif x==6:
    print("Your heart will skip a beat.")
  elif x==7:
    print("The fortune you search for is in another cookie.")
  elif x==8:
    print("Help! I'm being held prisoner in a Chinese bakery!")
  else:
    print("invalid")

fortune()
fortune()
fortune()
