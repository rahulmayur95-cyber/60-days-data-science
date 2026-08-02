def calculate_average(mark_list):
    total = sum(mark_list)
    average = total / len(mark_list)
    return average
def classify_grade(average):
    if average >= 75:
        return "Distinction"
    elif average >= 50:
        return "Pass"
    else:
        return "Fail"
Student_marks = []
number_of_subjects = int(input("Enter the number of subjects: "))
for i in range(number_of_subjects):
    mark = float(input("Enter the mark for subject " + str(i + 1) + ": "))
    Student_marks.append(mark)
    final_average = calculate_average(Student_marks)
    final_grade = classify_grade(final_average)
    print("\n--- Final Results ---")
    print("your average marks:", round(final_average, 2))
    print("your grade:", final_grade)