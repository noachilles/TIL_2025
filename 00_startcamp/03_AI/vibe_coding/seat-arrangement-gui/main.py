import eel
import random

eel.init('web')

@eel.expose
def arrange_seats(names, num_rows, num_cols, empty_positions):
    total_seats = num_rows * num_cols
    seats = [["" for _ in range(num_cols)] for _ in range(num_rows)]
    # 빈자리 좌표에 "(빈 자리)"를 먼저 채움
    for r, c in empty_positions:
        seats[r][c] = "(빈 자리)"
    # 남은 칸에 학생 무작위 배치
    students = names[:]
    random.shuffle(students)
    idx = 0
    for r in range(num_rows):
        for c in range(num_cols):
            if seats[r][c] == "" and idx < len(students):
                seats[r][c] = students[idx]
                idx += 1
    return seats

eel.start('index.html', size=(1280, 900))