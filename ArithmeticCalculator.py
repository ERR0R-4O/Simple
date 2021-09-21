import math

def calc():
  numOne = int(input("What is the first number of your problem?"))
  numTwo = int(input("What is the second number of your problem?"))
  numThree = input("What type of Math Problem is it, Addition, Subtraction, Multiplication, Division, Remainder, Exponents, or Factorials? Type exactly.")

  if numThree == 'Addition':
    print(numOne + numTwo)
  elif numThree == 'Subtraction':
    print(numOne - numTwo)
  elif numThree == 'Multiplication':
   print(numOne * numTwo)
  elif numThree == 'Division':
    print(numOne / numThree)
  elif numThree == 'Remainder':
    print(numOne % numTwo)
  elif numThree == 'Exponents':
    print(numOne ** numTwo)
  elif numThree == 'Factorials':
    thing = input("Which number do you want to use, the first or second? Type 1 for the first one or 2 for the second.")
    if thing == '1':
      print(math.factorial(numOne))
    elif thing == '2':
      print(math.factorial(numTwo))
    else:
      print("Not acceptable format. Wait for the program to restart and run again.")
  else:
    print("Not acceptable format. Wait for program restart and try again")

while True:
  calc()
