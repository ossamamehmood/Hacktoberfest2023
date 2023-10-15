def add(num1,num2):
    return num1+ num2

def sub(num1,num2):
    return num1-num2

def mul(num1,num2):
    return num1*num2

def div(num1,num2):
    return num1/num2




while True:
    
      print("Please select operation:\n"
            "1. Addition\n"
            "2. Subtraction\n"
            "3. Multiplication\n"
            "4. Division\n"
            "5. Exit\n")
      

      select = int(input("Select any operation : "))

      if select == 5:
           print("Exiting the calculator")
           break
      

      number1 = int(input("Enter first number : "))
      number2 = int(input("Enter second number : "))

      if select == 1:
            print(number1, "+", number2, "=", add(number1,number2))

      elif select == 2:
            print(number1, "-", number2, "=", sub(number1,number2))

      elif select == 3:
            print(number1, "*", number2, "=", mul(number1,number2))

      elif select == 4:
            print(number1, "/", number2, "=", div(number1,number2))
      else:
            print("Invalid selection")

      
