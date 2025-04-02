#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. The hat decides which of the four "Houses" each first-year student goes to:

#🦁 Gryffindor
#🦅 Ravenclaw
#🦡 Hufflepuff
#🐍 Slytherin

# Write code below 💖
Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0
print("Q1) Do you like Dawn or Dusk?")
print("1) Dawn")
print("2) Dusk")
question1= int(input('Enter your answer (1-4): '))
if question1==1:
  Gryffindor+=1
  Ravenclaw+=1
elif question1==2:
  Hufflepuff+=1
  Slytherin+=1
else:
  print("Wrong input")

question2=print("Q2) When I’m dead, I want people to remember me as:")
print("1 The Good")
print("2 The Great")
print("3 The Wise")
print("4 The Bold")

question2= int(input('Enter your answer (1-4): '))
if question2==1:
  Hufflepuff+=2
elif question2==2:
  Slytherin+=2
elif question2==3:
  Ravenclaw+=2
elif question2==4:
  Gryffindor+=2
else:
  print("Wrong input.")

question3=print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

question3= int(input('Enter your answer (1-4): '))
if question3==1:
  Slytherin+=4
elif question3==2:
  Hufflepuff+=4
elif question3==4:
  Gryffindor+=4
elif question3==3:
  Ravenclaw+=4
else:
  print("Wrong input")

print("Gryffindor:",Gryffindor)
print("Ravenclaw:",Ravenclaw)
print("Hufflepuff:",Hufflepuff)
print("Slytherin:",Slytherin)
