# List and Tuples does the same thing i.e. it allows multiple values and can be different data types
# But there is 1 difference that Tuple datatype is immutable i.e. data in a tuple is write protected.
# Also, the data in tuple is written using parenthesis and commas

values = (1, 3, "Abhay", 1.5)

print(values[1])

values[2] = "ABHAY"
print(values) # O/P : TypeError: 'tuple' object does not support item assignment
