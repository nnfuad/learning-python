f = open("TextForpy22.txt","w") # to write files(overwrite actually, erases all prev saved texts...)
f.write("I like learning python") # this func takes pointer to the end of the string added...we will understand it more in the next code where will read and write with w+/r+
#print(f.read()) # WONT WORK, CUZ IN W MODE
f.close()

f=open("TextForpy22.txt","r") # to read a file 
line1= f.readline() # adds an endline after reading each line also cursor moved like f.write
print(line1)
print(f.read()) # doesnt read anything except for the endline after
f.close()