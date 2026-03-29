while True:
    try:
        num = float(input("Enter number: "))
        
        if num == 0:
            print("Loop ended")
            break
    except ValueError:
        print("Error: Please enter a valid number.")