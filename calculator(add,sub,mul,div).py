#calculator [add,sub,mul,div]
name=input("hey what is name: ")
num1=int(input("enter your first num: "))
num2=int(input("enter your second num: "))
choice= input("Enter choice(add/sub/mul/div):").lower()
if choice == "add":
    print(name,"you has done using add =",num1+num2)
elif choice == "sub":
    print(name,"you had done using sub =",num1-num2)
elif choice == "mul":
    print(name,"you has done using mul =",num1*num2)
elif choice == "div":
    print(name,"you has done using div =",num1/num2)
else:
    "invalid"

