marks = [95, 98, 97, "maths"]
print(marks)  # Prints the entire list

print(marks[0])  # Prints the first element: 95
print(marks[1])  # Prints the second element: 98
print(marks[-2])  # Prints the second last element: 97
print(marks[1] + marks[-2])  # Adds the second and second last elements: 98 + 97 = 195

print(marks[0:-1])  # Prints from the first element to the second last element: [95, 98, 97]
print(marks[0:3])  # Prints from the first to the third element: [95, 98, 97]
print(marks[-1:-3])  # Prints an empty list since the start index is greater than the end index: []
print(marks[-2:-1])  # Prints the second last element: [97]
print(marks[-1:0])  # Prints an empty list since the start index is greater than the end index: []
print(marks[-2:2])  # Prints the second last element up to but not including the third element: [97]
	# •	print(marks): Prints the entire list.
	# •	print(marks[0]): Accesses the first element.
	# •	print(marks[1]): Accesses the second element.
	# •	print(marks[-2]): Accesses the second last element using negative indexing.
	# •	print(marks[1] + marks[-2]): Adds the second and second last elements. This works because both elements are integers.
	# •	print(marks[0:-1]): Slices the list from the first element to the second last element.
	# •	print(marks[0:3]): Slices the list from the first to the third element.
	# •	print(marks[-1:-3]): Attempts to slice the list but results in an empty list because the start index is greater than the end index.
	# •	print(marks[-2:-1]): Slices the list to include the second last element.
	# •	print(marks[-1:0]): Results in an empty list because the start index is greater than the end index.
	# •	print(marks[-2:2]): Slices the list from the second last element up to but not including the third element.


print(marks)
marks.append(99) #appends 99 at the end
print(marks)
marks.append("Fuad")
print(marks)
marks.insert(0,99) #inserts 99 at 0th index
print(marks)
marks.insert(5,"Hasin")
print(marks)
print(len(marks))
print(len(marks[2:5]))

print(99 in marks)
print((99 and "Fuad" ) in marks)
print((99 and "Gandhi" ) in marks)
marks.clear()
print(marks)


marks = [95, 98, 97, "maths",98]
marks.remove(98) # removes first occurance of 98
marks.pop(-3) #pops value at idx -3(97)
print(marks)