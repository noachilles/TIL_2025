class Theater():
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
        
    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            return "좌석 예약이 완료되었습니다."
        else:
            return "에약 가능한 좌석이 없습니다."
        
    
class MovieTheater(Theater):
    total_movies = 0
    
    def __init__(self, name, total_seats):
        super().__init__(name, total_seats)
        # reserved_seats가 없어서 오류가 발생
    
    def add_movie(self):
        MovieTheater.total_movies += 1
        return "영화 추가 성공"
    
    @staticmethod
    def description(self):
        print(f'영화관 이름: {self.name}\n총 좌석 수: {self.total_seats}\n예약된 좌석 수: {self.reserved_seats}\n총 영화 수: {MovieTheater.total_movies}')
        
if __name__ == '__main__':
    megabox = MovieTheater("메가박스",100)
    print(megabox.reserve_seat())
    print(megabox.reserve_seat())
    print(megabox.add_movie())
    MovieTheater.description(megabox)
    