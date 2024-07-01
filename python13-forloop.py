for i in range(100):
    print(i)
    i+=2
# Detailed Step-by-Step Execution

# 	1.	First Iteration:
# 	•	i starts at 0 (from the range(100)).
# 	•	print(i) prints 0.
# 	•	i += 2 increments i to 2.
# 	2.	Second Iteration:
# 	•	i is set to 1 (the next value from range(100)).
# 	•	print(i) prints 1.
# 	•	i += 2 increments i to 3.
# 	3.	Subsequent Iterations:
# 	•	The process repeats, but each time the loop starts, i gets the next value from range(100), ignoring the manual increment inside the loop.
# 	•	So, it prints the sequence 0, 1, 2, 3, …, 98, 99.

# Key Points

# 	•	Increment Inside Loop:
# 	•	The i += 2 inside the loop does not affect the next value of i in the for loop. The for loop assigns the next value from the range sequence to i on each iteration, overwriting any changes made inside the loop.
# 	•	This means i += 2 is effectively ignored in terms of the loop’s control variable.

for i in range(100,200,2):
    print(i)