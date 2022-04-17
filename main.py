import json
import os.path
from typing import Dict

from pyrh import Robinhood


def get_robinhood_login_json(path='~/.robinhood/login.json') -> Dict:
    with open(os.path.abspath(os.path.expanduser(path))) as fh:
        obj = json.load(fh)
    return obj


if __name__ == '__main__':
    rh = Robinhood()
    creds = get_robinhood_login_json()
    rh.login(username=creds['email'], password=creds['password'])
    del creds
    rh.print_quote("AAPL")
