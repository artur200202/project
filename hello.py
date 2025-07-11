print("Hello, world!")
print(2+5)
a = 5 
b = 3 
result= a + b
name='artur'
items=["bananna", "apples", "oranges"]
print("the sum of", a, "and", b, "is", result) 
print(type(a))
print(type(name))
print(type(items))

#we need users age
#we need to know if the person is 18+
#if age is met , then we ask if user has voting card
#if they do have then access granted
#if they dont have , then Id is required
#if user is not above 18 then user is to young

grade= 94
if grade >= 90:
  print("grade A")
elif grade >=80:
  print("grade B")
elif grade>= 70:
  print("grade C")
else: 
  print("keep trying")


age= 25
if age >= 18 and age<=60:
  print('you can work')
elif age<=18:
  print('you are to young')
elif age>=60:
  print ('you are to old ')

#find out the wheater is it sunny, rainy , or cold? use input
#if sunny then ask if its morning or afternoon? use input
#if its morning then wear glasses and a hat, and if its afternoon use sunscreen and stay hydarated
#if rainy do you have umbrella ? yes no 
#if yes great stay dry/ no , find shelter quickl;y
#if cold stay warm
'''
wheather= input("Is it sunny , rainy, or cold? : ")

if wheather== 'sunny':
  ask=input("if its morning, or afternoon?:")
  if ask == "morning" :
    print("wear sunglasses")
  else :
    print("Use sunscreen and stay hydrated")
elif wheather == "rainy":
  ask= input('do you have an unmbrella? :')
  if ask =='yes':
    print("stay dry")
  else:
    print("find shelter quickly")
else:
  print("stay warm!")
'''
'''
for i in range(1, 13):
  print(12*i)

j=1
while j <= 12:
  result = 12 * j
  print(result)
  j+=1
  '''
#ask user to enter a number
#if user enters a valid number any number,  then display multiplcation table from 1-12
#if its not avalid number then print an error message please enter valid number
#if the user types an exit then stop the program
#repeat the loop until user types exit-choose a number or write exit to quit
'''
while True:
  user= input ("enter a number or enter exit to leave:")
  if user == "exit":
    break
  if user.isdigit():
    for i in range(1, 13):
      result= int (user) *i
      print(result)
  else:
    print("its not valid, enter valid number")
  '''
age_str="25"
age_str= int(age_str)
age= age_str +5
print(age)

#Convert the float 6.7 to an integer and print the result

height = 6.7
height= int(height)
print(height)

value1=0
value="hello"
value2= bool(value1)
print(value2)
value3= bool(value)
print(value3)

