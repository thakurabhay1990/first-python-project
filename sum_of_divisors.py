# Calculate sum of divisor
def sum_of_divisors(number):
    sum = 0

    if(number < 2):
        return 0

    #
    for divisor in range(1,number+1):
        if number % divisor == 0:
            sum = sum + divisor
    return sum

print(sum_of_divisors(8))
print(sum_of_divisors(15))
print(sum_of_divisors(30))
print(sum_of_divisors(60))