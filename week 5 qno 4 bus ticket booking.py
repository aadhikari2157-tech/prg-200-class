class Bus:

    def __init__(self, route, total_seats):
        self.route = route
        self.total_seats = total_seats
        self.booked = {}
    
    