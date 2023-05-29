# Reading a content from a file via python.

file = open('one.txt')
print(file.read()) # Help you to read all contents of the file.

print(file.read(5)) # Print specific characters from the file.

print(file.readline()) # This will read 1 single line at a time.

print(file.readline())

file.close()


# Print all the contents of the file line by line using readline method with while loop
line = file.readline()
while line != "":
    print(line)
    line = file.readline()

file.close()


print(file.readlines()) # This will store the line in the list.
# # O/P : ['hi all,\n', 'this is a kreatos test.\n', '\n', 'Please ignore']
file.close()

# Print all the contents of the file line by line using readlines method with for loop
for line in file.readlines():
    print(line)