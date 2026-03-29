def print_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

try:
    num = int(input("Enter number: "))
    print_table(num)
    
except ValueError:
    print("Error: Please enter a valid integer.")