"""This module contains the Result class used to represent an auction result"""
import json
from auction.bid import Bid
from auction.json_obj import JsonObj


class Result(JsonObj):
    """
    Class to represent an auction result. E.g.
    [<Bid>]

    Attributes
    ----------
    data : list
        List of Bid objects

    Methods
    -------
    has_adjusted_bid(unit_name)
        Method to determine if this result has an adjusted bid for unit
        unit_name
    new_bid(bid, adjusted_bid)
        Method to add a new bid to this result

    """

    def __init__(self, **kwargs):
        super().__init__(list(), **kwargs)
        self._adjusted_bids = dict()
        self._bids = dict()

    def has_adjusted_bid(self, unit_name):
        """Method to determine if this result has an adjusted bid for unit
        unit_name

        Parameters
        ----------
        unit_name : str
            Unit name

        Returns
        -------
        bool
            True if this result has an adjusted bid for unit unit_name,
            False otherwise

        """
        return unit_name in self._adjusted_bids

    def new_bid(self, bid, adjusted_bid):
        """Method to add a new bid to this result. For a bid to be added the
        adjusted_bid for this bid has to be greater than any existing
        adjusted bids for the same bid unit.

        Parameters
        ----------
        bid : :obj:Bid
            Bid object
        adjusted_bid : float
            The adjusted bid value for this Bid

        """
        if self.has_adjusted_bid(bid.unit) and \
                self._adjusted_bids[bid.unit] > adjusted_bid:
            return
        # We have a new winner bid
        self._adjusted_bids[bid.unit] = adjusted_bid
        self._bids[bid.unit] = bid

    def default(self, o):
        """Custom json encoder for this class. It encodes any Bid objects
        from Result.data attribute

        Parameters
        ----------
        o : object
           Python object

        Returns
        -------
        str
           Serializable object for obj

        """
        if isinstance(o, Bid):
            return o.data
        return json.JSONEncoder.default(self, o)

    @property
    def data(self):
        """list:  Data containing a list of Bid objects"""
        return list(self._bids.values())
