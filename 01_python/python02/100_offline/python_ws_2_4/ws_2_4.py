class MovieTheater():
    total_movies = 0
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
        
    def __str__(self):
        return self.name

    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            print("좌석 예약이 성공적으로 완료되었습니다.")

    def current_status(self):
        print(f'{self.name} 영화관의 총 좌석 수: {self.total_seats}')
        print(f'{self.name} 영화관의 예약된 좌석 수: {self.reserved_seats}')
        
    @classmethod
    def add_movie(cls):
        cls.total_movies += 1
        return "영화가 성공적으로 추가되었습니다."        
       
    @staticmethod
    def description():
        print(f'총 영화 수: {MovieTheater.total_movies}')
        print("이 클래스는 영화관의 정보를 관리하고 좌석 예약 및 영화 추가 기능을 제공합니다.\n영화관의 이름, 총 좌석 수, 예약된 좌석 수, 총 영화 수를 관리합니다.")

megabox = MovieTheater("메가박스", 100)
cgv = MovieTheater("CGV", 150)

for i in range(2):
    megabox.reserve_seat()
cgv.reserve_seat()

print(MovieTheater.add_movie())
print(MovieTheater.add_movie())

megabox.current_status()
cgv.current_status()
MovieTheater.description()