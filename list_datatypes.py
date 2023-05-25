# List is a data type that allows multiple values and can be different data types
# List is same like how we have arrays in other languages in C, C++, Java etc.
values = [1, 3, "Abhay", 1.5]

# Now lets print the value from list
print(values[0])
print(values[3])

print(values[-1]) #If we want to print last index in the list here i.e. "1.5"

# When you want to print from 1st index to 3rd index. Note 3rd Index will be excluded here
print(values[1:3]) # O/P : [3, 'Abhay']

# If you want to insert "Thakur" after 2nd index in the above list
values.insert(3, "Thakur")
print(values) # O/P : [1, 3, 'Abhay', 'Thakur', 1.5]

# If you want to append value in the above list
values.append("Tester")
print(values) # O/P : [1, 3, 'Abhay', 'Thakur', 1.5, 'Tester']

# If you want to update the value in the list
values[2] = "ABHAY" # O/P : [1, 3, 'ABHAY', 'Thakur', 1.5, 'Tester']
print(values)

# If you want to delete the first index value
del values[0]
print(values) # O/P : [3, 'ABHAY', 'Thakur', 1.5, 'Tester']

