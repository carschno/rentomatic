class Transport:
    def __init__(self, price: float, seats: int, name: str = "", mileage: int = 0):
        self._price = price
        self._seats = seats
        self._available = True
        self._name = name if name else type(self).__name__
        self._mileage = mileage
        self._id = id(self)

    @property
    def price(self) -> float:
        return self._price

    @property
    def seats(self) -> int:
        return self._seats

    @property
    def name(self) -> str:
        return self._name

    @property
    def mileage(self) -> int:
        return self._mileage

    @property
    def id(self) -> int:
        return self._id

    @property
    def available(self) -> bool:
        return self._available

    @available.setter
    def available(self, available: bool):
        self._available = available

    def __str__(self):
        return """
        Type:   {}
        Price:  {}
        Seats:   {}
        Mileage:    {}
        Available:  {}
        ID: {}
        """.format(self.name, self.price, self.seats, self.mileage, self.available, self.id)


class Bike(Transport):
    def __init__(self, price: float = 5.0, seats: int = 1):
        super().__init__(price, seats)


class Boat(Transport):
    def __init__(self, price: float = 100.0, seats: int = 8):
        super().__init__(price, seats)


class Car(Transport):
    def __init__(self, price: float = 100.0, seats: int = 5):
        super().__init__(price, seats)


class Motorbike(Transport):
    def __init__(self, price: float = 75.0, seats: int = 2):
        super().__init__(price, seats)