class MovieTheater():
    def __init__(self, name, total_seats):
        self.name = name
        self.total_seats = total_seats
        self.reserved_seats = 0
        
    def __str__(self):
        return self.name

    def reserve_seat(self):
        if self.reserved_seats < self.total_seats:
            self.reserved_seats += 1
            print("좌석 예약이 완료되었습니다.")

    def current_status(self):
        print(f'총 좌석 수: {self.total_seats}')
        print(f'예약된 좌석 수: {self.reserved_seats}')
        

class VIPMovieTheater(MovieTheater):
    def __init__(self, name, total_seats, vip_seats):
        super().__init__(name, total_seats)
        self.vip_seats = vip_seats

    def reserve_vip_seat(self):
        if self.vip_seats:
            self.vip_seats -= 1
            print("VIP 좌석 예약이 완료되었습니다.")
        else:
            print("예약 가능한 VIP 좌석이 없습니다.")

    def reserve_seat(self):
        if self.vip_seats:
            self.reserve_vip_seat()
        else:
            super().reserve_seat()

megabox = VIPMovieTheater("메가박스", 100, 3)

for i in range(2):
    megabox.reserve_vip_seat()

for i in range(2):
    megabox.reserve_seat()

megabox.reserve_vip_seat()