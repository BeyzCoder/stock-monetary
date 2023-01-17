"""
This web scraping file is solely purpose for a specific web pages. The 
objective of this is to get the history prices of a stock. Depending on
the choice of the user.

Coded: Steven Baes
Date: 11 Jan, 2023
"""

from io import StringIO
from typing import Dict
import pandas as pd
import csv

import json     # For printing output in the terminal.

def transform(text: str) -> Dict:
    """
    Grab the csv text response from the web page that was download from weblink.

    Read a csv file and into a json file.

    @param text: The HTML text from an HTTP requests get.
    @return: Raw data from the csv text website.
    """
    # Read the response text and convert into a list.
    file_prices = StringIO(text)
    reader = csv.reader(file_prices)
    data = list(reader)
    names = data.pop(0)

    # Create a dataframe for fast selecting.
    df = pd.DataFrame(data, columns=names)

    # Change some of the columns type to numeric.
    for name in names[1:]:                          # Exclude the Date
        df[name] = pd.to_numeric(df[name])

    # Convert it into a json.
    data_json = { name : df[name].to_list() for name in names }

    return data_json

if __name__ == "__main__":
    # dev check code.
    # with open("test/samples/prices_O.csv") as handle:
    #     raw_data = transform(handle.read())
    #     # print(json.dumps(raw_data, indent=2))
    pass