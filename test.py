# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     output = []
#     abc = []
#     for X in range(x+1):
#         for Y in range(y+1):
#             for Z in range(z+1):
#                 if X+Y+Z != n:
#                     abc = [X,Y,Z]
#                     output.append(abc)
# print(output)


# def check_number_and_alphabet(num, alph):
#     if isinstance(num, int):
#         if len(str(num)) > 8:
#             print("Number has more than 8 digits.")
#         else:
#             print("Number is valid.")
#     else:
#         print("Invalid input. Please provide a number.")
#
#     if isinstance(alph, str):
#         if len(alph) > 10:
#             print("Alphabet string has more than 10 characters.")
#         else:
#             print("Alphabet string is valid.")
#     else:
#         print("Invalid input. Please provide an alphabet string.")
#
# # Example usage
# check_number_and_alphabet(123456789, "Hello World!")


# name = "abhay"
# name1 = "solan"
#
# temp = f"this is a {name} from {name1} city"
# print(temp)

'''
Python collections:
1. List
2. Tuple
3. Set
4. Dictionary
    -
'''

# lst = [1,2,3,4,5,6]
# # lst[3] = 55
# # var = lst.append(66)
# # lst.insert(4,99)
# # lst.remove(6)
# # lst.pop()
# # del lst[3]
# # del lst
# lst.clear()
# print(lst)

# age = int(input("Enter your age:"))
#
# if age > 18:
#     print("You can drive")
# elif age ==18:
#     print("You age is 18 and you are eligible to drive")
# else:
#     print("You are not eligible to drive")

# tuple = (1,2,3,"123",5,6)
# for tuples in tuple :
#     print(tuples)


# i=0
# while i<1000:
#     i = i + 1
#     if i == 78:
#         continue
#     print(i)

# class Employee:
#     def __init__(self, gname, gsalary):
#         self.name = gname
#         self.salary = gsalary
#
# test = Employee("Abhay", 1000)
# print(test.name)
# print(test.salary)

# with open("one.txt", "a") as f:
#     f.write("This is a new test")
#     f.writable()
#
# with open("one.txt", "r") as r:
#     test = r.read()
#     print(test)


# number_input = input("Please enter the number :- ")
# number = int(number_input)
#
# if number % 2 == 0:
#     print("Number is even Number")
# else:
#     print("Number is odd Number")


# i = 1
# while (i <= 10):
#     print(i)
#     i+=1

# Table in normal order
# number = input("Please enter your number : - ")
# i=1
# while (i<=10):
#     print(str(number) + " * " + str(i) + " = " + str(int(number)*i))
#     i+=1

# Table in Reverse order
# number = input("Please enter your number : - ")
# i= 10
# while (i>=1):
#     print(str(number) + " * " + str(i) + " = " + str(int(number)*i))
#     i-=1

# break statement

for i in range(1,11):
    if(i==5):
        break

    print(i)

