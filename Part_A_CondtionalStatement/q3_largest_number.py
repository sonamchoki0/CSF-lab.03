try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if num1 > num2:
        print(f"{num1} is larger")
    elif num2 > num1:
        print(f"{num2} is larger")
    else:
        print("Both numbers are equal")
        
except ValueError:
    print("Error: Please enter valid numbers.")