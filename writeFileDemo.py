# Read the file and store all the lines in the list
# Reverse the list back in the file
# Write the list back to the file

with open('one.txt', 'r') as reader:  # This line will opens your file and closes it. file = open('open.txt') & file.close() is not needed now.
    content = reader.readlines()  # Storing the initial list we captured in a variable
    reversed(content)  # Reversed the list content here
    with open('one.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)