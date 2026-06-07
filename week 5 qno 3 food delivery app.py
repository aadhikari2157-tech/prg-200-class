class DeliveryPartner:

    def __init__(self, name, partner_id, deliveries):
        self.name = name
        self.partner_id = partner_id
        self.deliveries = deliveries

    def total_earning(self):
        return 0
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Deliveries: {self.deliveries}")
        print(f"Total Earning: NPR {self.total_earning()}")
        print("-" * 30)

class BikeRider(DeliveryPartner):
    def __init__(self, name, partner_id, deliveries, km_travelled):
        super().__init__(name, partner_id, deliveries)
        self.km_travelled = km_travelled

        