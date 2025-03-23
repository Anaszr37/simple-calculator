# A simple Python calculator

while True:
    print("\n1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")
    choice = int(input("Enter Choice: "))

    if choice == 5:
        break

    num1 = float(input("Enter operand #1: "))
    num2 = float(input("Enter operand #2: "))

    if choice == 1:
<<<<<<< HEAD
        print("Result:", num1 + num2) #Corrected to addition
=======
        print("Result:", num1 + num2)
>>>>>>> 6f64d8be47df33cba696a072906bd890707d4f5f
elif choice == 2:
    print("Result:", num1 - num2)  # Corrected to subtraction

    elif choice == 3:
        print("Result:", num1 * num2)
    elif choice == 4:
        print("Result:", num1 / num2)