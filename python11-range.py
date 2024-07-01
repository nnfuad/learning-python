#range() is a func that takes int as argument and returns values from 0 to n-1...n might show in range but not included...more later in code

input1 = int(input("Enter a range: "))
print(range (input1))

#three kinda range in python..
#1.stop range:
for i in range(input1):
    print(i)

#2.range(start,stop):
stop = int(input("Enter where to stop (enter a number greater than " + str(input1) + "): "))
for i in range(input1,stop):
    print(i)

#3.range(start,stop,interval):
stop = int(input("Enter where to stop (enter a number greater than " + str(input1) + "): "))
inv=int(input("Enter interval between(enter a number greater than 1 to see effective result)"))
for i in range(input1 , stop, inv):
    
    print(i)