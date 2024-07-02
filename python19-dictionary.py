# dictionary is used when we have to use info in pairs...

marks= {"English" : 45 , "Biology" : 95 , "Fuad" : 31}
roll = {"Fuad":31 , "Hamim":32 ,"siam":34, "Fuad":300}
print(marks["English"])
roll["Hamim"]=31
roll["Fuad"]=32
print(roll)

# doesnt print repeated elements...

for i in roll:
    print(i)