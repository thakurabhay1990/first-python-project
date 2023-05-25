# print squares upto limit
# For e.g. :  limit = 30, output would be 1, 4, 9, 16, 25
def print_squares_upto_limit(limit):
    i =1
    while i * i < limit:
        print (i*i,end=" ")
        i = i + 1

print_squares_upto_limit(30)


# print cube upto limit
# For e.g. :  limit = 80, output would be 1, 8, 27, 64
def print_cubes_upto_limit(limit):
    i =1
    while i * i * i < limit:
        print (i*i*i, end=" ")
        i = i + 1

print_cubes_upto_limit(80)