def print_a_number_triangle(number):
    for j in range(1,number+1):
        for i in range(1,j+1):
            print(i, end=" ")
        print()

print_a_number_triangle(6)