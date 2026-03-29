
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

try:
    choice = int(input("Enter choice: "))
    
    if choice in [1, 2, 3, 4]:
        num1 = float(input("Enter two numbers: "))
        num2 = float(input(""))
        
        if choice == 1:
            result = num1 + num2
            print(f"Sum = {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"Difference = {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"Product = {result}")
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
                print(f"Quotient = {result}")
            else:
                print("Error: Division by zero!")
    else:
        print("Invalid choice!")
        
except ValueError:
    print("Error: Please enter valid numbers.")