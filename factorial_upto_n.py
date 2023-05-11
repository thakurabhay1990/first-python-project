number = 7
def factorial_upto_n(number):
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial * i
    return factorial

print("The factorial of", number, "is", factorial_upto_n(number))