# Grading System
def calculate_grade(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'
    
# User input and validation
while True:
    try:
        score = float(input("Enter the student's score (0-100): "))
        if 0 <= score <= 100:
            grade = calculate_grade(score)
            print(f"The student's grade is: {grade}")
            break
        else:
            print("Please enter a valid score between 0 and 100.")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the score.")
        
