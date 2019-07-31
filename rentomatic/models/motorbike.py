from rentomatic.models.transport import Transport


class Motorbike(Transport):
    def __init__(self, price: float = 75.0, seats: int = 2):
        super().__init__(price, seats)

