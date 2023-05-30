# try catch mechanism in python with customized error message

try:
    with open('oned.txt', 'r') as reader:
        reader.read()

except:
    print("There is a failure in try block")


# try catch mechanism in python that appears on the fly

try:
    with open('oned.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

finally: # this keyword can only be used when we have used try except block
    print("cleaning up resources")