#if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'audi':
        print(car.upper())  ------------> upper case
    else:
        print(car.title())  ------------ > first letter become upper case

#Check for equality

car = 'bmw'
var =car == 'Bmw'    ------------> False
print(var)


car = 'Bmw'
var =car == 'Bmw'    ------------> True
print(var)

car = 'bmw'
var =car.title() == 'Bmw'    ------------> True
print(var)

answer = 17
if answer != 42:
    print("That is not the correct answer. Please try again!")  --------------> not Equal

age = 25
var = age > 19    ---------> greater 
print(var)


age = 25
var = age < 19   ------------> lessthen
print(var)

age = 25
var = age != 19 ------------> not equal
print(var)


#using and check multiple condition

age_0 = 20 
age_1 = 21
var = age_0 >= 20 and age_1 >= 20     -----------> if one condition false it become fail
print(var)

#using or check multiple condition
age_0 = 20 
age_1 = 21
var = age_0 >= 2 or age_1 >= 33        --------------> if any condition pass you will get pass      
print(var)

#Checking whether a value is not in a list

banned_users = ['andrew', 'carolina', 'david']
user = 'marie'

if user not in banned_users:                     ----------------------->
    print(f"{user.title()}, you can post a response if you wish.")


age = 19
if age >= 20:
    print("You are old enough to vote!")
else:
    print("not equal")


#if-elif-else chain:

age = 15

if age <= 4:
    print("your admission is free of cost")
elif age <= 15:
    print("yor admission cost is $10")
else:
    print("your admission cost is $40" )


age = 12
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"your admission cost is {price}")

using multiple elif blocks
age = 64
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40

print(f"your age is {price}")


#testing multiple condicution

cars = ['audi', 'bmw', 'subaru', 'toyota']

if 'audi' in cars:
    print("adding audi")
if 'bmw' in cars:
    print("adding bmw")
if 'subar' in cars:
    print("adding subaru")

print("\n finishing making your cars")


cars = ['audi', 'bmw', 'subaru', 'toyota']

if 'audi' in cars:
    print("adding audi")
elif 'bmw' in cars:
    print("adding bmw")

print("\n finishing making your cars")

#Looping through all the keys in directory

var = {'name':'antrow','age':'22'}

for name in var.keys():     -----------> all keys
    print(name.title())

for name in var.values():   ------------> all Values
    print(name.title())

for key, value in var.items():     
    print(f"\nkey:{key}")
    print(f"value:{value}")

#using multi list:

var1 = ['ajith','mano','anish','poul']
var2 = ['ajith','mano','anish','badrai']

for var in var2:
    if var in var1:
        print(f"adding {var}")
    else:
        print(f"sorry, we dont have {var}")

print("\n finished making a pizza")

