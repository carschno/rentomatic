from rentomatic.models.transport import Transport


class Car(Transport):
    def __init__(self, price: float = 100.0, seats: int = 5):
        super().__init__(price, seats)

