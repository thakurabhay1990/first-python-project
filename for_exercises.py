# To find the number is a prime number?
# Prime number are the number which are divided by 1 OR by themselves only.
# For e.g. 5 => True, 7 => True, 11 => True, 6 => False

def is_prime(number):

    if(number < 2):
        return False

    #check if number is divisible by 2 to number-1
    for divisor in range(2,number):
        if number % divisor == 0:
            return False
    return True

print(is_prime(16))