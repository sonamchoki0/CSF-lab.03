try:
    n = int(input("Enter n: "))
    
    total = 0
    i = 1
    
    while i <= n:
        total += i
        i += 1
    
    print(f"Sum = {total}")
    
except ValueError:
    print("Error: Please enter a valid integer.")