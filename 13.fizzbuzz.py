#Fizz Buzz is a children's word game that teaches division. It's also a classic technical interview question at countless companies.
#For multiples of 3, print "Fizz" instead of the number
#For multiples of 5, print "Buzz" instead of the number
#For multiples of 3 and 5, print "FizzBuzz"
#im gonna use a for loop here with control flow

for i in range(1,101):
  if i%3==0 and i%5==0:
    print("FizzBuzz")
  elif(i%3==0):
    print("Fizz")
  elif(i%5==0):
    print("Buzz")
  else:
    print(i)
