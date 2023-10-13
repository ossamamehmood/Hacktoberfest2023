def add(num1,num2):
  return num1+num2
  
def sub(num1,num2):
  return num1-num2
  
def multi(num1,num2):
  return num1*num2

def div(num1,num2):
  try:
    return num1/num2
  except Exception as e:
    print(e)
    
def power(num1,num2):
  return num1**num2
  
def remain(num1,num2):
  return num1%num2

def select_op(choice):
  if (choice == '#'):
    return -1
  elif (choice == '$'):
      return 0
  elif (choice in ('+','-','*','/','^','%')):
    while (True):
      num1s = str(input("Enter first number: "))
      print(num1s)
      if num1s.endswith('$'):
        return 0
      if num1s.endswith('#'):
        return -1
        
      try:
        num1 = float(num1s)
        break
      except:
        print("Not a valid number, please enter again")
        continue
    
    while (True):
      num2s = str(input("Enter second number: "))
      print(num2s)
      if num2s.endswith('$'):
        return 0
      if num2s.endswith('#'):
        return -1
      try:  
        num2 = float(num2s)
        break
      except:
        print("Not a valid number, please enter again")
        continue
      
    if choice == '+':
      print("‣", num1, "+", num2, "=", add(num1, num2))
  
    elif choice == '-':
      print("‣", num1, "-", num2, "=", sub(num1, num2))
  
    elif choice == '*':
      print("‣", num1, "*", num2, "=", multi(num1, num2))
  
    elif choice == '/':
      print("‣", num1, "/", num2, "=", div(num1, num2))
      
    elif choice == '^':
      print("‣", num1, "^", num2, "=", power(num1, num2))
      
    elif choice == '%':
      print("‣", num1, "%", num2, "=", remain(num1, num2))
      
    else:
      print("Something Went Wrong")
  else:
    print("Unrecognized operation. Please enter again")
    
while True:
  print("Select operation")
  print("1.Add      : + ")
  print("2.Subtract : - ")
  print("3.Multiply : * ")
  print("4.Divide   : / ")
  print("5.Power    : ^ ")
  print("6.Remainder: % ")
  print("7.Terminate: # ")
  print("8.Reset    : $ ")
  
  # take input
  choice = input("Enter your choice(+,-,*,/,^,%,#,$): ")
  print(choice)
  if(select_op(choice) == -1):
    #program ends
    print("Done. Terminating...")
    exit()
