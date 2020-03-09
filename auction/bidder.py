"""This module contains the Bidder class used to decode a bidder configuration"""
from auction.json_obj import JsonObj


class Bidder(JsonObj):
    """
    Class to represent a bidder as defined in config.json. E.g.:
    {
            "name": "AUCT",
            "adjustment": -0.0625
    }

    Attributes
    ----------
    name : str
        Bidder name
    adjustment : float
        Bidder adjustment

    """

    def __init__(self, data="", **kwargs):
        """__init__ method.

        Parameters
        ----------
        data : dict
            A dictionary of Python decoded objects representing a Bidder
        **kwargs
            Keyword arguments passed to JsonObj parent class (used for encoding)

        """
        super().__init__(data, **kwargs)

    @property
    def name(self):
        """str:  Bidder name"""
        return self._data['name']

    @property
    def adjustment(self):
        """str:  Bidder adjustment"""
        return self._data['adjustment']
