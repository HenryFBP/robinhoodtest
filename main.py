import json
import os
from typing import Dict
from pyrhhfbp import Robinhood, dump_session, load_session

from someutils import user_prompt_yn

RH_CONFIG_PATH = os.path.abspath(os.path.expanduser('~/.robinhood/'))

if not os.path.exists(RH_CONFIG_PATH):
    os.mkdir(RH_CONFIG_PATH)

RH_LOGIN_CRED_PATH = os.path.join(RH_CONFIG_PATH, 'login.json')
RH_SESSION_JSON_PATH = os.path.join(RH_CONFIG_PATH, 'session.json')


def get_robinhood_login_json(path=RH_LOGIN_CRED_PATH) -> Dict:
    with open(path) as fh:
        obj = json.load(fh)
    return obj


def get_robinhood_from_disk_or_prompt(session_json_path, creds) -> Robinhood:
    if os.path.exists(session_json_path):
        rh = load_session(session_json_path)
        print("Loaded session from '{}'...\n"
              "Testing if it's valid... AAPL price = {}".format(
            session_json_path,
            rh.get_quote_list("AAPL", "symbol,last_trade_price")[0][1]
        ))
    else:
        print("We do not have a saved session. Using saved creds. you may be prompted for 2fa")
        rh = Robinhood(username=creds['email'], password=creds['password'], challenge_type='sms')

    print("rh.oauth.is_valid={}".format(rh.oauth.is_valid))
    if not rh.oauth.is_valid:
        print("We need to log in again :P")
        rh.login()

    return rh


if __name__ == '__main__':

    rh = get_robinhood_from_disk_or_prompt(RH_SESSION_JSON_PATH, creds=get_robinhood_login_json())

    if rh.oauth.is_valid:
        print("Saving our valid login session to {} so we don't have to login a bunch".format(
            RH_SESSION_JSON_PATH))
        dump_session(rh, RH_SESSION_JSON_PATH)

    # aaplprices = rh.get_quote_list("AAPL")
    xela_price = rh.quote_data('XELA')['last_extended_hours_trade_price']
    xela_amt = 3
    print("XELA: costs ${}".format(xela_price))

    yesmsg = "Yes, submit BUY order for {} XELA.".format(xela_amt)
    nomsg = "No, do not submit BUY order for {} XELA.".format(xela_amt)
    if user_prompt_yn(
            "Submit BUY order of {} XELA for ${:.4f} total?".format(xela_amt, (xela_amt * float(xela_price))),
            {
                'yes': yesmsg,
                'no': nomsg
            },
            successval=yesmsg):

        print("im BUYIIING XELA OOOOUGHHHHH @w@")

        rh.place_market_buy_order(instrument_URL='wewwers.com')

    else:
        print("k, not buying any XELA... stocks broke. understandable, have a great day")

    # rh.buy('youre mom')
