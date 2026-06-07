class Bus:

    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}
    
    def book_seat(self, seat_number, passenger_name):
        if seat_number in self.booked:
            print("Seat already booked")

        else:
            self.booked[seat_number] = passenger_name
            print(f"Seat {seat_number} booked for {passenger_name}")

            