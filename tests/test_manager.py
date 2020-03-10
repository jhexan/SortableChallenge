"""auction.manager unit tests"""
import os
import json
import pytest
from auction.manager import AuctionManager

_TEST_DATA_PATH = os.path.splitext(__file__)[0]
_CONFIG_FILE = "config.json"
_AUCTIONS_FILE = "auctions.json"


@pytest.fixture
def auction_mgr():
    """Setup code to create an auction_mgr instance"""
    with open(os.path.join(_TEST_DATA_PATH, _CONFIG_FILE), "r") as file:
        config = file.read()
    return AuctionManager(config)


def test_execute_auctions(auction_mgr):
    """
    Test to validate AuctionManager.execute_auctions
    """
    with open(os.path.join(_TEST_DATA_PATH, _AUCTIONS_FILE), "r") as file:
        results = auction_mgr.execute_auctions(file.read())
    results = json.loads(results)

    assert not len(results) == 0
    assert not results[0]  # unknown site
    assert not results[1]  # invalid bids
    print(_TEST_DATA_PATH)
    # multiple bids
    winning_bids = [{'bidder': 'bidder1', 'unit': 'banner', 'bid': 25},
                    {'bidder': 'bidder2', 'unit': 'sidebar', 'bid': 31.683}]
    multiple_bids = results[2]
    all_bids_found = True
    for bid in winning_bids:
        if bid in multiple_bids:
            # We found the bid
            multiple_bids.remove(bid)
        else:
            all_bids_found = False
            break
    assert not multiple_bids and all_bids_found
