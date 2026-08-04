import csv
from collections import Counter

input_file = "students.csv"
output_file = "grade_summary.txt"

grades = []

with open(input_file, mode="r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        grades.append(row["Grade"])

grade_counts = Counter(grades)


with open(output_file, mode="w") as file:
    file.write("--- GRADE SUMMARY REPORT ---\n")
    for grade, count in grade_counts.items():
        summary_line = f"Grade {grade}: {count} student(s)\n"
        file.write(summary_line)
        print(summary_line.strip())  

print(f"\nSummary successfully written to '{output_file}'!")