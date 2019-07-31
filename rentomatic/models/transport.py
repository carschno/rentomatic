class Transport:
    def __init__(self, price: float, seats: int, name: str = "", mileage: int = 0):
        self._price = price
        self._capacity = seats
        self._available = True
        self._name = name if name else type(self).__name__
        self._mileage = mileage
        self._id = id(self)

    @property
    def price(self) -> float:
        return self._price

    @property
    def capacity(self) -> int:
        return self._capacity

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
        Capacity:   {}
        Mileage:    {}
        Available:  {}
        ID: {}
        """.format(self.name, self.price, self.capacity, self.mileage, self.available, self.id)
