from rentomatic.models.transport import Transport


class Boat(Transport):
    def __init__(self, price: float = 100.0, seats: int = 8):
        super().__init__(price, seats, "boat")

