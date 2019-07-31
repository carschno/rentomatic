# Rent-o-matic

## Prerequisites

Python 3.x required.

No external library dependencies.

## Usage

Run:

```bash
python rent.py
```

This will print a list of available commands.

## Status

This will start a 'Rent-o-matic', and initialize it with 1-10 random available transports,
plus one random transport that is already rented out (i.e. not available).

The interactive interface allows to rent and return transports through their ids.
All commands are available through the `help` command.


Not done:
*  Money handling (change, check for price vs. available money)
*  UML diagrams
*  Unit test

Additional ideas for future improvements:
*  Make output more readable
*  Make IDs shorter for readability
*  Enable interaction with multiple users
*  Facilitate packaging with Python `setuptools`