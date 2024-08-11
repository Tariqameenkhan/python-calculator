# docker run -it or ti
# docker build -t

def add(x,y):
    total = x+y
    return total
def multiply(x,y):
    total = x*y
    return total
def divide(x,y): 
    total = x/y
    return total
def subtract(x,y):
    total = x-y
    return total
x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
operator = input("Please enter an operator (+, -, *, /): ")
if operator == '+':
    total = add(x,y)
    print(total)
elif operator == '-':
    total = subtract(x,y)
    print(total)
elif operator == '*':
    total = multiply(x,y)
    print(total)
elif operator == '/':
    total = divide(x,y)
    print(total)




#BASIC Calculator
#import sys
#input = sys.stdin.read
num1 = int(input("enter value 1:"))
num2 = int(input("enter value 2:"))
opr = input("Enter the op..(+,-,*,/,**,%,//)")

if opr=="+":
 print(num1+num2)   

elif opr=="-":
 print(num1-num2) 

elif opr=="*":
 print(num1*num2) 

elif opr=="/":
 print(num1/num2) 

elif opr=="**":
 print(num1**num2) 

elif opr=="%":
 print(num1%num2) 

elif opr=="//":
 print(num1//num2)

else:
 print("not found")









