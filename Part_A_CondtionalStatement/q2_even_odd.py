try:
    num = int(input("Enter a number: "))
    
    if num % 2 == 0:
        print(f"The number is even")
    else:
        print(f"The number is odd")
        
except ValueError:
    print("Error: Please enter a valid integer.")