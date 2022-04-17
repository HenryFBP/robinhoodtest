import json
import os
from typing import Dict
from pyrhhfbp import Robinhood, dump_session, load_session

from someutils import user_prompt_yn

LOGIN_CRED_PATH = os.path.abspath(os.path.expanduser('~/.robinhood/login.json'))
SESSION_PICKLE_PATH = os.path.abspath(os.path.expanduser('~/.robinhood/session.json'))


def get_robinhood_login_json(path=LOGIN_CRED_PATH) -> Dict:
    with open(path) as fh:
        obj = json.load(fh)
    return obj


def get_robinhood_object_pickle_or_creds(picklepath, creds) -> Robinhood:
    if os.path.exists(picklepath):
        rh = load_session(picklepath)
        print("Loaded session from '{}'...\n"
              "Testing if it's valid. AAPL price = {}".format(
            picklepath,
            rh.get_quote_list("AAPL", "symbol,last_trade_price")[0][1]
        ))
    else:
        print("We do not have a saved session.")
        rh = Robinhood(username=creds['email'], password=creds['password'], challenge_type='sms')

    print("rh.oauth.is_valid={}".format(rh.oauth.is_valid))
    if not rh.oauth.is_valid:
        print("We need to log in again :P")
        rh.login()

    return rh


if __name__ == '__main__':

    rh = get_robinhood_object_pickle_or_creds(SESSION_PICKLE_PATH, creds=get_robinhood_login_json())

    if rh.oauth.is_valid:
        print("Saving login session to {} so we don't have to login a bunch".format(
            SESSION_PICKLE_PATH))
        dump_session(rh, SESSION_PICKLE_PATH)

    # aaplprices = rh.get_quote_list("AAPL")
    xela_price = rh.quote_data('XELA')['last_extended_hours_trade_price']
    print("XELA: costs ${}".format(xela_price))

    if user_prompt_yn("Buy 1 XELA for {}?".format(xela_price)):
        print("im BUYIIING XELA OOOOUGHHHHH @w@")
    else:
        print("k, not buying")

    # rh.buy
