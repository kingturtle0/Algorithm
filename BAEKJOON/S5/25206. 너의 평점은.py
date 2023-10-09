grade = {'A+':4.5, 'A0':4.0, 'B+':3.5, 'B0':3.0, 'C+':2.5, 'C0':2.0, 'D+':1.5, 'D0':1.0, 'F':0.0}
total_credit = 0
sum_score = 0
for _ in range(20):
    name, credit, level = input().split()
    if level == 'P': continue
    total_credit += float(credit)
    sum_score += float(credit) * grade.get(level)

print(sum_score/total_credit)