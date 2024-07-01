a=float(input("Enter a the first number: "))
op=input("Enter a the operator: ")
b=float(input("Enter a the second number: "))

if op == "+":
    print(a+b)
elif op=="-":
    print(a-b)
elif op=="*":
    print(a*b)
elif op=="**":
    print(a**b)
elif op=="%":
    print(a%b)
elif op=="/" and int(b)!=0:
    print(a/b)
elif op =="/" and int(b)==0:
    print("Division by 0 not possible")
else:
    print("Invalid input")
    
