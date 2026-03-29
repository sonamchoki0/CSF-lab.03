def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

try:
    num = int(input("Enter number: "))
    
    if num < 0:
        print("Error: Factorial is not defined for negative numbers.")
    else:
        fact = factorial(num)
        print(f"Factorial = {fact}")
        
except ValueError:
    print("Error: Please enter a valid integer.")