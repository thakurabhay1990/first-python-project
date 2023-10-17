# PATTERN - 1
#
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5

for i in range(1,6): # This is an outer loop -> Rows
    for j in range(i): # this is an inner loop -> Column
        print(i, end="")
    print()


# PATTERN - 2
# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

for i in range(5,0,-1): # This is an outer loop -> Rows
    for j in range(i): # this is an inner loop -> Column
        print(i, end="")
    print()
