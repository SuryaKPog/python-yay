height=int(input("What is your height?:"))
credits=int(input("What is your amount of credits?:"))
if height>137 and credits>10:
  print("Enjoy the ride!")
elif not height>137 and credits>10:
  print("You are not tall enough to ride.")
elif not credits>10 and height>137:
  print("You don't have enough credits.")
else:
  print("you have not met either requirement :(")
