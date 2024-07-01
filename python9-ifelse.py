# in c or cpp or java we used {} to determine if else block here we do "Identation"
# indentation on 4 spaces(1 tab)

input = int(input("Enter you age: "))

if input >= 18:
    print("You are an adult")
    print("You can vote...")
elif input > 3 and input < 18:
    print("You cant vote")
else:
    print("Why are you on computer?")

print("End of if loop cuz of no indentation")
