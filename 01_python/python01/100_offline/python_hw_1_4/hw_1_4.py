'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.
students = dict({"Alice": 85,
   "Bob": 78,
   "Charlie": 92,
   "David": 88,
   "Eve": 95})

s = 0
for k in students.keys():
   s += students[k]
avg = s / len(students)

above_students = [student for student in students.keys() if students[student] >= 80]

sorted_students = sorted(students.items(), key=lambda x: -x[1])
max_score = sorted_students[0][1]
min_score = sorted_students[-1][1]
diff_score = max_score - min_score


print(f'1. 학생들의 이름과 점수를 딕셔너리에 저장')
print(f'students type: {type(students)}')
print(f'학생들의 이름과 점수: {students}')
print(f'2. 모든 학생의 평균 점수: {avg:.2f}')
print(f'3. 기준 점수 (80점) 이상을 받은 학생 수: {above_students}')
print(f'4. 점수 순으로 정렬:')
for student in sorted_students:
   print('{}: {}'.format(student[0], student[1]))

print(f'5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: {diff_score}')
print(f'6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:')
for student in students:
   if students[student] > avg:
      print(f'{student} 학생의 점수({students[student]})는 평균 이상입니다.')
   else:
      print(f'{student} 학생의 점수({students[student]})는 평균 이하입니다.')
