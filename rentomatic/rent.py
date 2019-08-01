import random
from typing import List

from rentomatic.controls.rentomatic import Rentomatic, random_transports
from rentomatic.models.transport import Transport


class Rent:
    def __init__(self, money: float = 500):
        self._money = money
        self._rented = list()  # type: List[Transport]
        self._rentomatic = Rentomatic()
        self.index = 1

        # Initialize with 1-10 random transports
        for transport in random_transports(k=random.randrange(1, 10, 1)):
            self._rentomatic.add_transport(transport)

        # Add one transport that is already rented and not available
        transport = random_transports(k=1)[0]
        transport.available = False
        self._rentomatic.add_transport(transport)

    @property
    def money(self) -> float:
        return self._money

    @property
    def rented(self) -> List[Transport]:
        return self._rented

    @staticmethod
    def print_help():
        print(
            """Available commands:
            
            help    this output
            status  see your status
            list    see a list of transports
            list avail  see a list of available transports
            list <name> see a list of available transports of type <name>
            info    <id>    show info about vehicle with <id>
            rent <id>    rent transport with <id>
            return <id>   return transport <id>
            exit    exit programme
            """
        )

    def __str__(self):
        return """
        Money:  {}
        Rented transports:  {}
        """.format(self.money, [str(transport) for transport in self.rented])

    def main(self):
        self.print_help()
        command = ""
        while command != "exit":
            try:
                command = input().strip()
                if command == 'help':
                    self.print_help()
                elif command == 'status':
                    print(str(self))
                elif command == 'list':
                    for transport in self._rentomatic.transports:
                        print(str(transport))
                elif command == 'list avail':
                    for transport in self._rentomatic.available_transports():
                        print(str(transport))
                elif command.startswith('list '):
                    name = command.split(" ")[1]
                    self._rentomatic.available_transport_name(name)
                elif command.startswith("info "):
                    t_id = self._extract_id(command)
                    if t_id is not None:
                        print(str(self._rentomatic.get_by_id(t_id)))
                elif command.startswith("rent "):
                    t_id = self._extract_id(command)
                    if t_id is not None:
                        t = self._rentomatic.rent(t_id)
                        self._rented.append(t)
                        self._money -= t.price
                elif command.startswith("return "):
                    t_id = self._extract_id(command)
                    if t_id is not None:
                        try:
                            transport = next((t for t in self._rented if t.id == t_id))
                            self._rentomatic.return_transport(transport)
                            self._rented.remove(transport)
                        except StopIteration:
                            print("You have not rented a transport with ID '{}'".format(t_id))
                else:
                    print("Unknown command. Type 'help' to see valid commands.")
            except Exception as e:
                print(str(e))

    @staticmethod
    def _extract_id(command: str):
        id_string = command.split(" ")[1]
        try:
            id_int = int(id_string)
            return id_int
        except ValueError:
            print("Invalid ID: '{}'".format(id_string))
            return None


if __name__ == '__main__':
    Rent().main()
