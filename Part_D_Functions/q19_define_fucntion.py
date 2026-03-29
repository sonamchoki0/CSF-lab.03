def add(a, b):
    return a + b

try:
    print("Enter two numbers: ", end="")
    num1, num2 = map(float, input().split())
    result = add(num1, num2)
    print(f"Sum = {result}")
    
except ValueError:
    print("Error: Please enter valid numbers.")