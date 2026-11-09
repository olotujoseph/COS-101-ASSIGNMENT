# Student Result and Progression Program

# Accept student details
student_name = input("Enter student name: ")

coursework = float(input("Enter coursework score (out of 30): "))
examination = float(input("Enter examination score (out of 70): "))

# Validate scores
if coursework < 0 or coursework > 30:
    print("Error: Coursework score must be between 0 and 30.")

elif examination < 0 or examination > 70:
    print("Error: Examination score must be between 0 and 70.")

else:
    # Calculate total
    total = coursework + examination

    # Assign grades
    if total >= 70:
        grade = "A"
    elif total >= 60:
        grade = "B"
    elif total >= 50:
        grade = "C"
    elif total >= 45:
        grade = "D"
    elif total >= 40:
        grade = "E"
    else:
        grade = "F"

    # Determine progression
    if total >= 50:
        decision = "Pass"
    else:
        decision = "Resit required"

    # Display result summary
    print("\nSTUDENT RESULT SUMMARY")
    print("------------------------------")
    print(f"Name: {student_name}")
    print(f"Coursework: {coursework:.2f} / 30")
    print(f"Examination: {examination:.2f} / 70")
    print(f"Total: {total:.2f} / 100")
    print(f"Grade: {grade}")
    print(f"Decision: {decision}")
