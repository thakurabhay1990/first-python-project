# Logic to printing a pattern 1 - Forward Pattern
n = int(input("Enter the value : "))
for i in range(n): # This is an outer loop -> Rows
    for j in range(i+1): # this is an inner loop -> Column
        print("*", end="")
    print()

# Logic to printing a pattern 2 - Reverse Pattern
n = int(input("Enter the value : "))
for i in range(n,0,-1): # This is an outer loop -> Rows
    for j in range(i,0,-1): # this is an inner loop -> Column
        print("*", end="")
    print()