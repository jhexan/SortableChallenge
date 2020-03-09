"""This module contains the Bid class used to decode an auction bid"""
from auction.json_obj import JsonObj


class Bid(JsonObj):
    """
    Class to represent an auction bid. E.g.:
    {
        "bidder": "AUCT",
        "unit": "banner",
        "bid": 35
    }

    Attributes
    ----------
    bidder : str
        Bidder name
    unit : str
        Auction unit name
    bid : float
        Bid amount

    """

    def __init__(self, data="", **kwargs):
        """__init__ method.

        Parameters
        ----------
        data : dict
            A dictionary of Python decoded objects representing a Bid
        **kwargs
            Keyword arguments passed to JsonObj parent class (used for encoding)

        """
        super().__init__(data, **kwargs)

    @property
    def bidder(self):
        """str: Bidder name"""
        return self._data['bidder']

    @property
    def unit(self):
        """str: Auction unit name"""
        return self._data['unit']

    @property
    def bid(self):
        """float: Bid amount"""
        return self._data['bid']
