## show first n even numbers from 0

def printEven(a):
    for i in range(0,(2*a),2):
        print(i)

a = int(input("Enter How many even numbers you want to print: "))
printEven(a)

## show first n odd numbers starting from 1

def printOdd(a):
    for j in range(1,(2*a),2):
        print(j)

b = int(input("Enter How many odd numbers you want to print: "))
printOdd(b)