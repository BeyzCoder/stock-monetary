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
def fetch(url: str, freq: str, params: Dict=None, headers: Dict=None) -> str:
    """
    Send out a request get to the url.

    @param url: The url that will be send out a request.
    @return: response text of the request.
    """
    if freq == "A":
        resp = req.get(url, params=params, headers=headers)
    else:
        resp = req.get(url, params=params, headers=headers)
        resp = req.get(resp.url+"?freq="+freq, params=params, headers=headers)
    if resp.status_code == 200:
        return resp.text
    return ""

def get_statement(symbol: str, state: Statement, freq: str, form: str) -> Dict:
    """
    Grab the financial statement of the company from the user's chosen ticker symbol.

    This function work around the functions of the financial.py file.

    @param symbol: The query input of the user.
    @param state: The three choices financial statement.
    @return: Usable data for analytical and logical.
    """
    # TODO: Must check if state url passed right.
    result = fetch(state.format(symbol), freq, params=None, headers=None)
    # Check if the requests return nothing
    if result == "":
        return {}
    
    # Building the data.
    raw_data = financial.parse(result)
    cleaned = financial.cleanse(raw_data)

    if form == "dataframe":
        cleaned = financial.form_dataframe(cleaned)

    return cleaned

def get_price(symbol: str) -> Dict:
    """
    TODO
    """
    # Build the params and headers for the request.
    # For now default params.
    params = {
        "range" : "1y",
        "interval" : "1d",
        "events" : "history"
    }

    headers = {
        "USER-AGENT" : "Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36"
    }
    
    data = { "Message" : "The lists are correspond to one another." }
    result = fetch(URL_HISTORY_PRICE.format(symbol), "A", params=params, headers=headers)
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