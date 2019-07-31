import logging
from typing import List, Iterable, Tuple

import random

from rentomatic.models.bike import Bike
from rentomatic.models.boat import Boat
from rentomatic.models.car import Car
from rentomatic.models.motorbike import Motorbike
from rentomatic.models.transport import Transport


class Rentomatic:
    def __init__(self, transports: List[Transport] = None):
        if transports is None:
            self._transports = list()
        else:
            self._transports = transports

    @property
    def transports(self) -> List[Transport]:
        return self._transports

    def add_transport(self, transport: Transport):
        self._transports.append(transport)

    def available_transports(self) -> List[Transport]:
        return [transport for transport in self.transports if transport.available]

    def available_transport_name(self, name: str) -> List[Transport]:
        return [transport for transport in self.available_transports() if transport.name == name]

    def get_by_id(self, id: int) -> Transport:
        try:
            return next(transport for transport in self.transports if transport.id == id)
        except StopIteration:
            raise ValueError("Transport with id '{}' does not exist.".format(id))

    def rent(self, id: int) -> Transport:
        transport = self.get_by_id(id)
        if transport.available:
            return transport
        else:
            raise UnavailableError(transport)

    @staticmethod
    def return_transport(transport: Transport):
        transport.available = True
        logging.info("{} with id {} has been returned.".format(transport.name, transport.id))


def random_transports(types: Tuple = (Bike, Boat, Car, Motorbike), k: int = 1) \
        -> List['Transport']:
    return [klass() for klass in random.choices(types, k=k)]


class UnavailableError(Exception):
    def __init__(self, transport: Transport):
        message = "Transport '{}' is not available.".format(str(transport))
        super().__init__(message)


class PriceError(Exception):
    def __init__(self, price_diff: float, transport: Transport):
        message = "Not enough money to rent a '{}', you need {} more.".format(transport.name,
                                                                              abs(price_diff))
        super().__init__(message)
