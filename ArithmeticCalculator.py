def calc():
  numOne = int(input("What is the first number of your problem?"))
  numTwo = int(input("What is the second number of your problem?"))
  numThree = input("What type of Math Problem is it, Addition, Subtraction, Multiplication, Division, Remainder, or Exponents? Type exactly.")

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
  else:
    print("Not acceptable format. Restart program and run again.")

while True:
  calc()
