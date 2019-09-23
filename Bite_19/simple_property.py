"""
Write a simple Promo class. Its constructor receives a name str 
and expires datetime.

Add a property called expired which returns a bool.

Checkout the tests and datetime module for more info. Have fun!
"""

from datetime import datetime

NOW = datetime.now()


class Promo:
    # Constructor
    # Type check Python 3.6 >
    def __init__(self, name: str, expires: datetime = NOW):
        self.name = name
        self.expires = expires
    
    # Use decorator to change method to property
    # Called Promo.expired instead of Promo.expired()
    @property
    def expired(self) -> bool:
        # If today is later than the expired
        # Return True
        return datetime.now() > self.expires
