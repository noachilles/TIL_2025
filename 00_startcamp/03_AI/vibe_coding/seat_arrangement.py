import random

def read_names_from_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            names = [line.strip() for line in file if line.strip()]
        return names
    except FileNotFoundError:
        print("파일을 찾을 수 없습니다.")
        return []

def arrange_seats(names, num_rows, num_cols):
    total_seats = num_rows * num_cols
    # 학생 수가 부족하면 빈 자리 추가
    if len(names) < total_seats:
        names += ["(빈 자리)"] * (total_seats - len(names))
    # 학생이 더 많으면 초과 학생은 제외
    elif len(names) > total_seats:
        names = names[:total_seats]
    random.shuffle(names)
    # 2차원 리스트로 변환
    seats = []
    idx = 0
    for r in range(num_rows):
        row = []
        for c in range(num_cols):
            row.append(names[idx])
            idx += 1
        seats.append(row)
    return seats

def print_seats(seats):
    print("무작위 자리 배치 결과:")
    for r, row in enumerate(seats, start=1):
        row_display = []
        for c, name in enumerate(row, start=1):
            row_display.append(f"{(r-1)*len(row)+c}. {name}")
        print(" | ".join(row_display))

def main():
    filename = 'students.txt'
    names = read_names_from_file(filename)
    if not names:
        return
    try:
        num_rows = int(input("행(row) 수를 입력하세요: "))
        num_cols = int(input("열(column) 수를 입력하세요: "))
    except ValueError:
        print("숫자를 입력하세요.")
        return
    seats = arrange_seats(names, num_rows, num_cols)
    print_seats(seats)

if __name__ == "__main__":
    main()