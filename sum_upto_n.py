# Program for sum of numbers upto n ?
# For e.g. 1+2+3+4+5 = 15 -> this is the sum

def sum_upto_n(number):
    sum = 0
    for i in range(1,number+1):
        sum = sum + i
    return sum

print(sum_upto_n(4))