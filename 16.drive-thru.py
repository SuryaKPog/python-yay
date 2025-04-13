def welcome():
  print("Hello! Welcome to McDonald's")
  print('🍔 Cheeseburger')
  print('🍟 Fries')
  print('🥤 Soda')
  print("🍦 Ice Cream")
  print("🍪 Cookie")

welcome()


x=int(input("Enter your choice of food"))

def get_item():
  if x==1:
    print('🍔 Cheeseburger')
  elif x==2:
    print("🍟 Fries")
  elif x==3:
    print('🥤 Soda')
  elif x==4:
    print('🍦 Ice Cream')
  elif x==5:
    print('🍪 Cookie')
  else:
    print("Invalid input")

get_item()
