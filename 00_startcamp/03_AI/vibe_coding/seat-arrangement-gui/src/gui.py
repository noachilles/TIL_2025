from tkinter import Tk, Label, Entry, Button, filedialog, messagebox, Frame
import os
import random
from seat_logic import arrange_seats  # 자리 배치 함수 import

class SeatArrangementGUI:
    def __init__(self, master):
        master.title("자리 정하기")
        master.configure(bg='skyblue')
        master.geometry("600x550")

        self.title_label = Label(master, text="자리 정하기", font=("Arial Rounded MT Bold", 24), bg='skyblue')
        self.title_label.pack(pady=(20, 5))


        self.row_label = Label(master, text="행(row) 수:", bg='skyblue')
        self.row_label.pack()
        self.row_entry = Entry(master)
        self.row_entry.pack(pady=5)

        self.col_label = Label(master, text="열(column) 수:", bg='skyblue')
        self.col_label.pack()
        self.col_entry = Entry(master)
        self.col_entry.pack(pady=5)

        self.file_button = Button(master, text="학생 목록 파일 선택", command=self.load_file)
        self.file_button.pack(pady=10)

        self.info_label = Label(master, text="", bg='skyblue', fg='red', font=("Arial Rounded MT Bold", 12))
        self.info_label.pack(pady=5)

        self.submit_button = Button(master, text="자리 배치", command=self.submit)
        self.submit_button.pack(pady=5)

        self.seat_frame = Frame(master, bg='skyblue')
        self.seat_frame.pack(pady=10)

        self.selected_file = None
        self.students = []

        # 빈 자리 선택 관련 변수
        self.empty_seats_to_select = 0
        self.selected_empty_positions = []
        self.empty_seat_labels = []
        self.last_seat_state = None  # 빈 자리 상태 저장

    def load_file(self):
        self.selected_file = filedialog.askopenfilename(title="학생 목록 파일 선택", filetypes=(("Text files", "*.txt"), ("All files", "*.*")))
        if self.selected_file:
            with open(self.selected_file, encoding="utf-8") as f:
                self.students = [line.strip() for line in f if line.strip()]
            messagebox.showinfo("파일 선택", f"선택한 파일: {os.path.basename(self.selected_file)}\n학생 수: {len(self.students)}명")

    def submit(self):
        for widget in self.seat_frame.winfo_children():
            widget.destroy()

        try:
            num_rows = int(self.row_entry.get())
            num_cols = int(self.col_entry.get())
            if not self.selected_file or not self.students:
                raise ValueError("학생 목록 파일을 선택하세요.")
        except ValueError as e:
            messagebox.showerror("입력 오류", str(e))
            return

        x = num_rows * num_cols
        y = len(self.students)

        self.empty_seats_to_select = x - y
        self.selected_empty_positions = getattr(self, "selected_empty_positions", [])
        self.empty_seat_labels = []

        if x < y:
            self.info_label.config(text="모두 앉을 수 없습니다.", fg='red')
            return
        elif self.empty_seats_to_select > 0:
            # 빈 자리가 모두 선택된 경우, 무작위 배치
            if hasattr(self, "last_seat_state") and self.last_seat_state and len(self.last_seat_state) == self.empty_seats_to_select:
                self.assign_students_to_seats(shuffle=True)
            else:
                self.info_label.config(text=f"빈 자리: {self.empty_seats_to_select}개를 클릭해서 선택하세요.", fg='blue')
                self.display_empty_seats(num_rows, num_cols)
        else:
            self.info_label.config(text="모든 학생이 자리에 앉았습니다!", fg='green')
            seats = arrange_seats(self.students, num_rows, num_cols)
            self.display_seats(seats)

    def display_empty_seats(self, num_rows, num_cols):
        # 기존 좌석/스크린 라벨 제거
        for widget in self.seat_frame.winfo_children():
            widget.destroy()
        # 스크린 라벨 추가 (맨 윗줄 중앙)
        self.screen_label = Label(
            self.seat_frame, text="스크린",
            font=("Arial Rounded MT Bold", 14),
            bg="white", fg="#1976D2", width=15, height=2, relief="ridge", bd=3
        )
        self.screen_label.grid(row=0, column=0, columnspan=num_cols, pady=(0, 20))
        self.empty_seat_labels = []
        self.selected_empty_positions = []
        for r in range(num_rows):
            row_labels = []
            for c in range(num_cols):
                label = Label(
                    self.seat_frame,
                    text="(빈 자리)",
                    width=10,
                    height=2,
                    relief="groove",
                    bg="white",
                    font=("Arial Rounded MT Bold", 11)
                )
                # row=r+1로 변경: 스크린 아래부터 좌석 시작
                label.grid(row=r+1, column=c, padx=5, pady=5)
                label.bind("<Button-1>", lambda e, row=r, col=c: self.select_empty_seat(row, col))
                row_labels.append(label)
            self.empty_seat_labels.append(row_labels)

    def select_empty_seat(self, row, col):
        if (row, col) in self.selected_empty_positions:
            return  # 이미 선택된 자리
        if self.empty_seats_to_select <= 0:
            return
        self.empty_seat_labels[row][col].config(bg="#FFD1DC")  # 귀여운 분홍색으로 표시
        self.selected_empty_positions.append((row, col))
        self.empty_seats_to_select -= 1
        self.info_label.config(text=f"빈 자리: {self.empty_seats_to_select}개 남음", fg='blue')
        if self.empty_seats_to_select == 0:
            # 빈 자리 상태 저장
            self.last_seat_state = list(self.selected_empty_positions)
            self.info_label.config(text="빈 자리가 모두 선택되었습니다!\n이제 '자리 배치' 버튼을 다시 눌러주세요.", fg='green')

    def assign_students_to_seats(self, shuffle=False):
        num_rows = int(self.row_entry.get())
        num_cols = int(self.col_entry.get())
        total_seats = num_rows * num_cols
        seats = [["" for _ in range(num_cols)] for _ in range(num_rows)]

        # 빈 자리 먼저 지정
        for (r, c) in self.last_seat_state:
            seats[r][c] = "(빈 자리)"

        # 학생 이름을 빈 자리가 아닌 곳에 무작위로 배치
        students = self.students[:]
        if shuffle:
            random.shuffle(students)
        student_idx = 0
        for r in range(num_rows):
            for c in range(num_cols):
                if seats[r][c] == "":
                    seats[r][c] = students[student_idx]
                    student_idx += 1

        # 좌석 표시 갱신
        for widget in self.seat_frame.winfo_children():
            widget.destroy()
        self.display_seats(seats)

    def display_seats(self, seats):
        # 기존 좌석/스크린 라벨 제거
        for widget in self.seat_frame.winfo_children():
            widget.destroy()
        num_cols = len(seats[0]) if seats else 0
        # 스크린 라벨 추가 (맨 윗줄 중앙)
        self.screen_label = Label(
            self.seat_frame, text="스크린",
            font=("Arial Rounded MT Bold", 14),
            bg="white", fg="#1976D2", width=15, height=2, relief="ridge", bd=3
        )
        self.screen_label.grid(row=0, column=0, columnspan=num_cols, pady=(0, 20))
        for r, row in enumerate(seats):
            for c, name in enumerate(row):
                seat_label = Label(
                    self.seat_frame,
                    text=name,
                    width=10,
                    height=2,
                    relief="groove",
                    bg="white" if name != "(빈 자리)" else "#FFD1DC",
                    font=("Arial Rounded MT Bold", 11)
                )
                # row=r+1로 변경: 스크린 아래부터 좌석 시작
                seat_label.grid(row=r+1, column=c, padx=5, pady=5)