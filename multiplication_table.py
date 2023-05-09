def print_multiplication_table(table,start=5,end=10):
    for i in range(start,end+1):
        print(f"{table} * {i} = {table*i}")

print_multiplication_table(23)