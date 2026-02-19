
grade_point = {
    "A+": 4.5, 
    "A0": 4.0,
    "B+": 3.5,
    "B0": 3.0,
    "C+": 2.5,
    "C0": 2.0,
    "D+": 1.5,
    "D0": 1.0,
    "F": 0.0
}
total_score_multiply_grade_point = 0
total_sum_score = 0
for _ in range(20):
    title, score, grade = input().split(" ")
    if grade != "P":
        score = float(score)
        total_score_multiply_grade_point += score * grade_point[grade]
        total_sum_score += score
print(round(total_score_multiply_grade_point / total_sum_score, 4))