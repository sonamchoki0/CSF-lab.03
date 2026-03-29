try:
    marks = float(input("Enter marks: "))
    
    if marks >= 80:
        grade = "A"
    elif marks >= 60:
        grade = "B"
    elif marks >= 40:
        grade = "C"
    else:
        grade = "Fail"
    
    print(f"Grade {grade}")
    
except ValueError:
    print("Error: Please enter valid marks.")