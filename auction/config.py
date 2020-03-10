"""This module contains the Config class used to decode data in config.json"""
from auction.bidder import Bidder
from auction.site import Site
from auction.json_obj import JsonObj


class Config(JsonObj):
    """
    Class used to decode data in config.json. This class uses the Site and
    Bidder JsonObj decoders to decode bidder and site elements from the
    configuration data. E.g.: { "sites": [<Site>], "bidders": [<Bidder>] }

    Attributes
    ----------
    sites : list
        List of Site objects in this config
    bidders : list
        List of Bidder objects in this config

    Methods
    -------
    has_site(site_name)
        Method to determine if this configuration has a site named site_name
    has_bidder(bidder_name)
        Method to determine if this configuration has a bidder named
        bidder_name
    get_adjustment(bidder_name)
        Method to get the adjustment value for a bidder
    get_site(site_name)
        Method to get a site object by name

    """

    def __init__(self, data="", **kwargs):
        """__init__ method.

        Parameters
        ----------
        data : dict
            A dictionary of Python decoded objects representing a config json
        **kwargs
            Keyword arguments passed to JsonObj parent class (used for
            encoding)

        """
        super().__init__(data, **kwargs)
        # Store data as dictionary for faster access
        # Also, only store elements of the correct type
        self._sites = {site.name: site
                       for site in self._data['sites']
                       if isinstance(site, Site)}
        self._bidders = {bidder.name: bidder
                         for bidder in self._data['bidders']
                         if isinstance(bidder, Bidder)}

    @property
    def sites(self):
        """list:  List of Site objects in this config"""
        return self._sites

    @property
    def bidders(self):
        """list:  List of Bidder objects in this config"""
        return self._bidders

    def has_site(self, site_name):
        """Method to determine if this config has a site named site_name

        Parameters
        ----------
        site_name : str
            Site name

        Returns
        -------
        bool
            True if this config has a site with name site_name, False otherwise

        """
        return site_name in self._sites

    def has_bidder(self, bidder_name):
        """Method to determine if this config has a bidder named bidder_name

        Parameters
        ----------
        bidder_name : str
            Bidder name

        Returns
        -------
        bool
            True if this config has a bidder with name bidder_name,
            False otherwise

        """
        return bidder_name in self._bidders

    def get_adjustment(self, bidder_name):
        """Method to get the adjustment value for a bidder

        Parameters
        ----------
        bidder_name : str
            Bidder name

        Returns
        -------
        float
            Bidder adjustment value

        """
        return self.bidders[bidder_name].adjustment

    def get_site(self, site_name):
        """Method to get a site object matching site_name

        Parameters
        ----------
        site_name : str
            Site name

        Returns
        -------
        :obj:Site
            Site object with name site_name

        """
        return self.sites[site_name]

    @staticmethod
    def _object_hook(json_dict):
        """Custom json decoder for this class. It can decode any Bidder,
        Site and Config object elements present in json_dict

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
            return Config(json_dict)
        if JsonObj._is_object(Bidder, json_dict):
            return Bidder(json_dict)
        if JsonObj._is_object(Site, json_dict):
            return Site(json_dict)
        return json_dict
