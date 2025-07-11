#add an exit condition  to quit the program
#add while true:loop so user can keep calcualtring unyil they type exit
def add(a,b):
  return a + b

def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b

def divide(a,b):
  return a / b


print("welcome to smart calculator!")
print("choose an option: +, -, *, /")
while True:
  operation = input(" what do you want to do (exit, help, history, +, -, *, /): ")
  
  if operation == "exit":
    break
  else: 
    
    try: 
      num1 = input("enter the first number: ")
      num2= input("enter the second number: ")
      num1 = float(num1)
      num2 = float(num2)

      if operation == "+": 
        print("Result: ", add(num1, num2) )
      elif operation == "-":
        print("Result: ", subtract(num1, num2))
      elif operation == "*":
        print("Result: ", multiply(num1, num2))
      elif operation == "/":
        if num2 != 0: 
          print("Result: ", divide(num1, num2))
        else: 
         print("Error: cannot divide by zero.")
      else  : 
        print("Invalid operation. Use  +, -, *, /.  ")
    
    except ValueError:
      print("Error: please enter valid numbers.")
    