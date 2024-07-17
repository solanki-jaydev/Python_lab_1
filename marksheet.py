
def calculate_marksheet(subject_marks):
    total = sum(subject_marks)
    average = total / len(subject_marks)
    
    if average >= 90:
        grade = 'A+'
    elif average >= 80:
        grade = 'A'
    elif average >= 70:
        grade = 'B'
    elif average >= 60:
        grade = 'C'
    elif average >= 50:
        grade = 'D'
    else:
        grade = 'F'
    
    return total, average, grade


subject_marks = []
for i in range(5):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    subject_marks.append(mark)


total_marks, average_marks, grade = calculate_marksheet(subject_marks)


print(f"Total marks: {total_marks}")
print(f"Average marks: {average_marks}")
print(f"Grade: {grade}")

