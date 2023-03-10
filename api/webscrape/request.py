"""
This file will do the connection to the web page and will hold the HTML text. This
will combine the function on the financial.py file to create the raw_data.

Coded: Steven Baes
Date: 30 Dec, 2022
"""
import sys
import os

sys.path.append(os.getcwd())

from config import Statement, URL_HISTORY_PRICE
from . import financial, prices
from typing import Dict, Optional
import requests as req

import json     # For printing output in the terminal.

# TODO: Must able to catch what type of status code.
def fetch(url: str, **kwargs: Dict) -> str:
    """
    Send out a request get to the url.

    @param url: The url that will be send out a request.
    @return: response text of the request.
    """
    content = {"params" : None, "headers" : None}
    if "params" in kwargs and "headers" in kwargs:
        content["params"] = kwargs["params"]
        content["headers"] = kwargs["headers"]

    if "freq" in kwargs:
        resp = req.get(url, **content)
        resp = req.get(resp.url+"?freq="+kwargs["freq"], **content)
    else:
        resp = req.get(url, params=content["params"], headers=content["headers"])
    
    if resp.status_code == 200:
        return resp.text
    
    return ""

def get_statement(symbol: str, state: Statement, **kwargs: Dict) -> Dict:
    """
    Grab the financial statement of the company from the user's chosen ticker symbol.

    This function work around the functions of the financial.py file.

    @param symbol: The query input of the user.
    @param state: The three choices financial statement.
    @return: Usable data for analytical and logical.
    """
    # TODO: Must check if state url passed right.
    result = ""
    if "freq" in kwargs:
        result = fetch(state.format(symbol), freq=kwargs["freq"])
    else:
        result = fetch(state.format(symbol))

    # Check if the requests return nothing
    if result == "":
        return {}
    
    # Building the data.
    raw_data = financial.parse(result)
    cleaned = financial.cleanse(raw_data)

    if "setup" in kwargs:
        cleaned = financial.form_dataframe(cleaned)

    return cleaned

def get_price(symbol: str, range: str = "1y", interval: str = "1d", event: str = "history") -> Dict:
    """
    TODO
    """
    # Build the params and headers for the request.
    # For now default params.
    params = {
        "range" : range,
        "interval" : interval,
        "events" : event
    }

    headers = {
        "USER-AGENT" : "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
    }
    
    data = { "Message" : "The lists are correspond to one another." }
    result = fetch(URL_HISTORY_PRICE.format(symbol), params=params, headers=headers)
    # Check if the requests return nothing
    if result == "":
        return {}
    
    raw_data = prices.transform(result)
    data.update(raw_data)
    return data

if __name__ == "__main__":
    # dev check code.
    # data = get_statement("GOOG", Statement.URL_INCOME_STATEMENT.value)
    # # print(json.dumps(data, indent=2))

    # data = get_price("O")
    # print(json.dumps(data, indent=2))
    pass