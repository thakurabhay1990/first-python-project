number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))

print("\n1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")

choice = int(input("Choose operation : "))


if choice==1:
    result=number1+number2
elif choice==2:
    result=number1-number2
elif choice==3:
    result=number1/number2
elif choice==4:
    result=number1*number2
else:
    print("No a valid choice")

print(result)