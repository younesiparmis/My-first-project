first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
operators = input("which one do you want to use? +, *, //, -: ")
if operators == "+":
    print(first_number + second_number)
elif operators == "*":
    print(first_number * second_number)
elif operators == "//":
    print(first_number // second_number)
elif operators == "-":
    print(first_number - second_number)
else:
    print("The operator is invalid.")