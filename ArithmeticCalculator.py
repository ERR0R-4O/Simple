import math

def calc():
  numOne = int(input("What is the first number of your problem?(x)"))
  numTwo = int(input("What is the second number of your problem?(y)"))
  numThree = input("Please type code for any following function: AD for Addition, SUB for Subtraction, MUL for Multiplication, DIV for Division, LOG for Base 10 LOG, EX for Exponents, MOD for Modulo")

  if numThree == 'AD':
    print(numOne + numTwo)
  elif numThree == 'SUB':
    print(numOne - numTwo)
  elif numThree == 'MUL':
   print(numOne * numTwo)
  elif numThree == 'DIV':
    print(numOne / numThree)
  elif numThree == 'LOG':
    logb10=math.log10(x)
    print(logb10)
  elif numThree == 'EX':
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
    print("Please enter on of the above functions. ")

while True:
  calc()
  
  repeat()
  
  def repeat():
    repeat_program=input('''Do you want to calculate again, Yes or No?''')
    
    if repeat_program == 'Yes':
        calculate()
    elif repeat_program == 'No':
        print('Thanks for using my calculator.')
    else:
        again()
