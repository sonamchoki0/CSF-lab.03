try:
    print("Enter three numbers: ", end="")
    num1, num2, num3 = map(float, input().split())
    
    if num1 >= num2:
        if num1 >= num3:
            largest = num1
        else:
            largest = num3
    else:
        if num2 >= num3:
            largest = num2
        else:
            largest = num3
    
    print(f"{largest} is the largest number")
    
except ValueError:
    print("Error: Please enter valid numbers.")