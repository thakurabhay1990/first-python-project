str = "AbhayThakurLearning.com"
str1 = "QA Testing Platform"
str3 = "AbhayThakur"

print(str[1]) # O/P : b

print(str[0:5]) # O/P : Abhay (if you want substring in python)


print(str + str1) # O/P : AbhayThakurLearning.comQA Testing Platform (to concatenate of 2 strings)


print(str3 in str) # O/P : True (to check if String 3 is present in string)

print(str.split(".")) # O/P : ['AbhayThakurLearning', 'com'] (when you want to split string in the form of list)

var = str.split(".")
print(var) # O/P : ['AbhayThakurLearning', 'com'] (same as line 15)
print(var[0]) # O/P : AbhayThakurLearning


str4 = "  great  "
print(str4.strip()) # The white spaces will be removed from str4 from both left and right.
print(str4.lstrip()) # The white spaces will be removed from str4 from left side.
print(str4.rstrip()) # The white spaces will be removed from str4 from right side.