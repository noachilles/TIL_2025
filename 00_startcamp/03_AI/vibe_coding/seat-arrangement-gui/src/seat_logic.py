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
    if len(names) < total_seats:
        names += ["(빈 자리)"] * (total_seats - len(names))
    elif len(names) > total_seats:
        names = names[:total_seats]
    return names, total_seats

def compare_students_to_seats(names, num_rows, num_cols):
    arranged_names, total_seats = arrange_seats(names, num_rows, num_cols)
    return len(arranged_names), total_seats, arranged_names