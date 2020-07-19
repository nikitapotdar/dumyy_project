print("This is program to add two numbers")
try :
    x = input("key in the first number : ")
    y = input("key in the second number : ")
    x = int(x)
    y = int(y)
except :
         print("alert : input onlt integer")
else :      
    z=x+y
    print("the value of sum : ",z)
