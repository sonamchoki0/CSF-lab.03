def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "odd"

try:
    num = int(input("Enter number: "))
    result = check_even_odd(num)
    print(f"The number is {result}")
    
except ValueError:
    print("Error: Please enter a valid integer.")