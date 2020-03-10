"""This module contains the Site class used to decode a site configuration"""
from auction.json_obj import JsonObj


class Site(JsonObj):
    """
    Class to represent an auction site as defined in config.json. E.g.:
    {
            "name": "houseofcheese.com",
            "bidders": ["AUCT", "BIDD"],
            "floor": 32
    }

    Attributes
    ----------
    name : str
        Site name
    bidders : list
        List of bidders allowed to bid on this site
    floor: float
        Minimum bid allowed on this site

    Methods
    -------
    has_bidder(bidder_name)
        Method to determine if this site has a bidder named bidder_name

    """

    def __init__(self, data="", **kwargs):
        """__init__ method.

        Parameters
        ----------
        data : dict
            A dictionary of Python decoded objects representing a Site
        **kwargs
            Keyword arguments passed to JsonObj parent class (used for
            encoding)

        """
        super().__init__(data, **kwargs)

    @property
    def name(self):
        """str:  Bidder name"""
        return self._data['name']

    @property
    def bidders(self):
        """list:  List of bidders allowed to bid on this site"""
        return self._data['bidders']

    @property
    def floor(self):
        """float:  Minimum bid allowed on this site"""
        return self._data['floor']

    def has_bidder(self, bidder_name):
        """Method to determine if this site has a bidder named bidder

        Parameters
        ----------
        bidder_name : str
            Bidder name

        Returns
        -------
        bool
            True if this Site has a bidder with name bidder_name,
            False otherwise

        """
        return bidder_name in self.bidders
