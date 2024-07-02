f= open("TextForpy23.txt","w+")
f.write("Hello This is written with w+ mode that overwrites whatever was written before...")
print(f.read()) # this line isnt gonna print anything cuz the pointer/cursur is at the end of first string
# rather we have to use readline()
print(f.readline())
f.close()