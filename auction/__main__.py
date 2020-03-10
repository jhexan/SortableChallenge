"""__main__ module executed when module is run with -m.

The module executes auctions from standard input and prints the results to
screen as a JSON formatted string

Example
-------
    $ cp /path/to/config/config.json /path/to/module/auction
    $ python -m /path/to/module/auction < auctions.json

Notes
-----
All inputs (auctions and config.json) are assumed to be well-formed
(e.g. all fields are present and are of the
expected types)

"""
import sys
import os
from auction.manager import AuctionManager

_CONFIG_FILE = 'config.json'
"""str: Constant to config file name"""
_CONFIG_PATH = os.path.dirname(os.path.realpath(__file__))
"""str: Constant to store config path as __main__.py path"""


def _get_config():
    """Method to parse config file _CONFIG_PATH/_CONFIG_FILE and return
    contents

    Returns
    -------
    str
       config.json content as a string

    """
    config = ""
    try:
        with open(os.path.join(_CONFIG_PATH, _CONFIG_FILE), "r") as file:
            config = file.read()
    except OSError as err:
        print("Cannot read config file: {0}".format(err))
    return config


def execute_auctions(auctions):
    """Method to execute auctions and to print the results to screen

    Parameters
    ----------
    auctions : str
        Auctions as a json string

    """
    config = _get_config()
    if config:
        auction_mgr = AuctionManager(config)
        print(auction_mgr.execute_auctions(auctions))


if __name__ == '__main__':
    execute_auctions(sys.stdin.read())
