print("welcome to smart calculator!")
print("choose an option: +, -, *, /")
operation = input("enter the operation: ")
num1 = input("enter the first number: ")
num2= input("enter the second number: ")

try: 
  num1 = float(num1)
  num2 = float(num2)

  if operation == "+": 
    print("Result: ", num1 + num2 )
  elif operation == "-":
    print("Result: ", num1 - num2)
  elif operation == "*":
    print("Result: ", num1 * num2)
  elif operation == "/":
    if num2 != 0: 
      print("Result: ", num1 / num2)
    else: 
      print("Error: cannot divide by zero.")
  else: 
    print("Invalid operation. Use  +, -, *, /.  ")

except ValueError:
  print("Error: please enter valid numbers.")
    