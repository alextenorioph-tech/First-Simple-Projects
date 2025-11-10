student_name = []
quiz_score = []
exam_score = []
attendance_score = []
seatwork_score = []

try:
    num_students = int(input("how many student to process? "))
except ValueError:
    print("please enter a valid number")

for i in range(num_students):
    print("\n")
    name = input("students name: ")
    student_name.append(name)

    try:
        quiz = float(input("quiz score: "))
        exam = float(input("exam score: "))
        attendance = float(input("attendance score: "))
        seatwork = float(input("seatwork score: "))
    except ValueError:
        print("please enter valid scores")
        continue

    quiz_score.append(quiz)
    exam_score.append(exam)
    attendance_score.append(attendance)
    seatwork_score.append(seatwork)

final_grades = []  
total_grade = []
highest_grade = []
lowest_grade = []

for i in range(len(student_name)):
    grade = (quiz_score[i] * 0.10) + (exam_score[i] * 0.40) + (attendance_score[i] * 0.05) + (seatwork_score[i] * 0.45)
    final_grades.append(grade)  
    total_grade += grade

    if grade > highest_grade:
        highest_grade = grade
    if grade < lowest_grade:
        lowest_grade = grade

average_grade = total_grade / len(final_grades) 

print("\n")
print("----class summary----")
print("\n")
for i in range(len(student_name)):
    print(f"{student_name[i]} final grade: {final_grades[i]:.2f}")
print("\n")  
print("----Overall----")
print("\n")
print(f"class average: {average_grade:.2f}")
print(f"highest grade: {highest_grade:.2f}")
print(f"lowest grade: {lowest_grade:.2f}")
