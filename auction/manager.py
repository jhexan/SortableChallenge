"""This module contains the AuctionManager class that stores configurations
and runs auctions """
from auction.auction import Auction
from auction.config import Config
from auction.bid import Bid
from auction.result import Result
from auction.json_obj import JsonObj


class AuctionManager:
    """
    Class that executes auctions based on a stored Config object

    Attributes
    ----------

    Methods
    -------
    execute_auctions(auctions_json)
        Method to execute auctions, passed in as a json string, and return the
        corresponding results

    """

    def __init__(self, config_json):
        """__init__ method.

        Parameters
        ----------
        config_json : str
            A json str instance containing the auction config.json. E.g.
            '{
                "sites": [
                    {
                        "name": "houseofcheese.com",
                        "bidders": ["AUCT", "BIDD"],
                        "floor": 32
                    }
                ],
                "bidders": [
                    {
                        "name": "AUCT",
                        "adjustment": -0.0625
                    },
                    {
                        "name": "BIDD",
                        "adjustment": 0
                    }
                ]
            }'

        """
        # Assume valid configurations
        self._config = JsonObj.loads(Config, config_json)

    def execute_auctions(self, auctions_json):
        """Method to execute individual auctions and to construct auction
        result objects. The return is a list of results as a json string.

        Parameters
        ----------
        auctions_json : str
            A json str instance containing the auctions to be executed. E.g.:
            '[
                {
                    "site": "houseofcheese.com",
                    "units": ["banner", "sidebar"],
                    "bids": [
                        {
                            "bidder": "AUCT",
                            "unit": "banner",
                            "bid": 35
                        },
                        {
                            "bidder": "BIDD",
                            "unit": "sidebar",
                            "bid": 60
                        },
                        {
                            "bidder": "AUCT",
                            "unit": "sidebar",
                            "bid": 55
                        }
                    ]
                }
            ]'

        Returns
        -------
        str
            A json str representing the auction results. E.g.:
            '[
                [
                    {
                        "bidder": "AUCT",
                        "bid": 35,
                        "unit": "banner"
                    },
                    {
                        "bidder": "BIDD",
                        "bid": 60,
                        "unit": "sidebar"
                    }
                ]
            ']

        """
        results = list()
        for auction in JsonObj.loads(Auction, auctions_json):
            results.append(self._execute_auction(auction))
        # return auction results as a json string
        return JsonObj.dumps(Result, results)

    def _get_adjusted_bid(self, site, auction, bid):
        """This method calculates the adjusted bid value for a valid bid
        with the following formula: adjusted bid = bid + (abs(bid) *
        adjustment)

        Parameters
        ----------
        site : :obj:Site
            Site object
        auction : :obj:Auction
            Auction object
        bid : :obj:Bid
            Bid object

        Returns
        -------
        float
            Adjusted bid value if the bid is valid, None otherwise

        """
        if self._is_valid_bid(site, auction, bid):
            # Adjusted bid is bid + (abs(bid) * adjustment)
            return bid.bid + (abs(bid.bid) *
                              self._config.get_adjustment(bid.bidder))
        return None

    def _is_valid_bid(self, site, auction, bid):
        """Determines if a bid is valid. A bid is invalid if the bidder is
        unknown, or a bidder is not permitted to bid on this site, or the
        bid is for an ad unit not involved with this auction.

        Parameters
        ----------
        site : :obj:Site
            Site object
        auction : :obj:Auction
            Auction object
        bid : :obj:Bid
            Bid object

        Returns
        -------
        float
            True if the bid is valid, False otherwise

        """
        return \
            isinstance(bid, Bid) and \
            self._config.has_bidder(bid.bidder) and \
            site.has_bidder(bid.bidder) and \
            auction.has_unit(bid.unit)

    def _is_valid_auction(self, auction):
        """Determines if an auction is valid. An auction is invalid if the
        site is unrecognised

        Parameters
        ----------
        auction : :obj:Auction
            Auction object

        Returns
        -------
        float
            True if the auction is valid, False otherwise

        """
        return \
            isinstance(auction, Auction) and \
            self._config.has_site(auction.site)

    def _execute_auction(self, auction):
        """Method to execute an auction and return its result.

        Parameters
        ----------
        auction : :obj:Auction
            Auction object

        Returns
        -------
        :obj:Result
            Auction Result object

        """
        result = Result()
        if self._is_valid_auction(auction):
            # if we have a valid auction determine the site
            site = self._config.get_site(auction.site)
            for bid in auction.bids:
                # For each bid in this auction get the adjusted bid
                adjusted_bid = self._get_adjusted_bid(site, auction, bid)
                if adjusted_bid is not None and \
                        adjusted_bid > max(site.floor, 0):
                    # If we have a valid bid add it to the result
                    result.new_bid(bid, adjusted_bid)
        # Return auction result data
        return result.data
