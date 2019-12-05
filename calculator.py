#To MAKE A CALCULATOR

n1=float(input("enter the first number:"))
oper=input("Enter the operator:")
n2=float(input("enter the second number:"))
if oper=="+" :
    print(n1+n2)
elif oper=="-" :
    print(n1 - n2)
elif oper=="*" :
    print(n1 * n2)
elif oper=="/" :
    print(n1 / n2)
else:
    print("invalid entry")


