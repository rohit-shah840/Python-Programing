#This if for the and opertation 
a=True
b= True

if a and b:
    print("Welcome to the if and else phython ")
else:
    print("This is the else block ")


#this is for the or condition with if and else

a=input("Enter the number : ")
b = input("Entert the second num : ")

if a>b or b>a:
    print("the greater element is "+a)
elif a==b:
    print("Both are equal and values is "+b)
else:
    print("The greater is "+b)

#not operator
x=True
y =False
var1=5
var2=6
if var1!=var2:
    print("true")
if not x:
    print("hello x ")
elif not y:
    print("Hello y")   
else: print("hello no body")     