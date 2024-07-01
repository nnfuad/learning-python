#this is a comment 

# and for precedence and associativity theres like a huge chart...chech th channel for it...https://t.me/+Z5c33IghqiI3ZDJl

# in simple terms u can remember like : PMDR AS (left to right)...
print(9*4/2%4) #left to right # 2
print(9/4%2*4) #left to right # 0

#yeah, its not 0, you wanna know why?
	# Division: 9 / 4
	# •	This evaluates to 2.25.
	# 2.	Modulo: 2.25 % 2
	# •	This evaluates to 0.25 because 2.25 divided by 2 gives a remainder of 0.25.
	# 3.	Multiplication: 0.25 * 4
	# •	This evaluates to 1.0.

print(9+4/3*4%2)# left to right(from 4/3) then addition # 9
#yeah, its not 9 baby... its not truncating to int...
#rather
#    1.	Division: 4 / 3
# 	•	This evaluates to approximately 1.3333.
# 	2.	Multiplication: 1.3333 * 4
# 	•	This evaluates to approximately 5.3333.
# 	3.	Modulo: 5.3333 % 2
# 	•	This evaluates to 1.3333 because 5.3333 divided by 2 leaves a remainder of 1.3333.
# 	4.	Addition: 9 + 1.3333
# 	•	This evaluates to 10.3333.

# So, the expression 9 + 4 / 3 * 4 % 2 evaluates to approximately 10.3333.