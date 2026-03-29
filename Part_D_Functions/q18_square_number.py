def square(num):
    return num * num

try:
    num = float(input("Enter number: "))
    result = square(num)
    print(f"Square = {result}")
    
except ValueError:
    print("Error: Please enter a valid number.")