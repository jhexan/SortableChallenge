"""This module contains the Auction class used to decode an auction"""
from auction.json_obj import JsonObj
from auction.bid import Bid


class Auction(JsonObj):
    """
    Class to represent an auction. E.g.
    {
        "site": "houseofcheese.com",
        "units": ["banner", "sidebar"],
        "bids": [<Bid>]
    }

    Attributes
    ----------
    site : str
        Site name
    units : list
        List of unit names in this auction
    bids : list
        List of Bid objects in this auction

    Methods
    -------
    has_unit(unit_name)
        Method to determine if this auction has a unit named unit_name

    """

    def __init__(self, data="", **kwargs):
        """__init__ method.

        Parameters
        ----------
        data : dict
            A dictionary of Python decoded objects representing an auction
        **kwargs
            Keyword arguments passed to JsonObj parent class (used for encoding)

        """
        super().__init__(data, **kwargs)

    @property
    def site(self):
        """str:  Site name"""
        return self._data['site']

    @property
    def units(self):
        """list:  List of unit names in this auction"""
        return self._data['units']

    @property
    def bids(self):
        """str:  List of Bid objects in this auction"""
        return self._data['bids']

    def has_unit(self, unit_name):
        """Method to determine if this auction has a unit named unit_name

        Parameters
        ----------
        unit_name : str
            Unit name

        Returns
        -------
        bool
            True if this auction has a unit with name unit_name, False otherwise

        """
        return unit_name in self.units

    @staticmethod
    def _object_hook(json_dict):
        """Custom json decoder for this class. It can decode any Bid and Auction object elements present in json_dict

        Parameters
        ----------
        json_dict : dict
            Python dictionary with standard type elements

        Returns
        -------
        dict
           Python dictionary with decoded elements

        """
        # We're assuming valid data
        if JsonObj._is_object(__class__, json_dict):
            return Auction(json_dict)
        if JsonObj._is_object(Bid, json_dict):
            return Bid(json_dict)
        return json_dict
