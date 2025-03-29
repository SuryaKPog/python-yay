import random
print("===================")
print("Rock Paper Scissors")
print("===================")
print("1) ✊")
print("2) ✋")
print("3) ✌️")

num=int(input("Pick a number: "))

print("You chose: ", end="")
if num == 1:
    print("✊")
elif num == 2:
    print("✋")
else:
    print("✌️")

if num!=1 and num!=2 and num!=3:
   print("Invalid Input")

ram=random.randint(1,3)

print("CPU chose: ", end="")
if ram == 1:
    print("✊")
elif ram == 2:
    print("✋")
else:
    print("✌️")
    
if(num==1 and ram==1):
   print("Its a Tie!")
elif(num==2 and ram==2):
   print("Its a Tie!")
elif(num==3 and ram==3):
   print("Its a Tie!")
elif(num==1 and ram==3):
   print("The player won!")
elif(num==1 and ram==2):
   print("The computer won!")
elif(num==2 and ram==3):
   print("The computer won!")
elif(num==2 and ram==1):
   print("The player won!")
elif(num==3 and ram==1):
   print("The player won!")
elif(num==3 and ram==1):
   print("The computer won!")
else:
   print("Invalid")
