number1 = int(input("Enter Number 1 : "))
number2 = int(input("Enter Number 2 : "))

print("1 - Add")
print("2 - Subtract")
print("3 - Divide")
print("4 - Multiply")
print("5 - Exit")

choice = int(input("Choose operation : "))

while (choice !=5):
    if choice==1:
        result=number1+number2
    elif choice==2:
        result=number1-number2
    elif choice==3:
        result=number1/number2
    elif choice==4:
        result=number1*number2
    elif choice==5:
        print("Exit! Thank you.")
    else:
        print("Not a valid choice")

    print(result)

    choice = int(input("Choose operation : "))

print("Thank you")