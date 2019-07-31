from rentomatic.models.transport import Transport


class Bike(Transport):
    def __init__(self, price: float = 5.0, seats: int = 1):
        super().__init__(price, seats)
