student_score = {
    "ahmed": 60,
    "nader": 90,
    "mahmoud": 80,
    "omar": 70,
}
for key in student_score:
    if student_score[key] >= 90:
        student_score[key] = "A"
    elif student_score[key] >= 80:
        student_score[key] = "B"
    elif student_score[key] >= 70:
        student_score[key] = "C"
    else:
        student_score[key] = "D"

for key in student_score:
    print(key)
    print(student_score[key])
