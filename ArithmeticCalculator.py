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
  else:
    print("Please enter on of the above functions. ")
while True:
  calc()
  
  repeat()
  
  def repeat():
    repeat_program=input('''Do you want to calculate again, Yes or No?''')
    
    if calc_again.upper() == 'Yes':
        calculate()
    elif calc_again.upper() == 'No':
        print('Thanks for using my calculator.')
    else:
        again()
