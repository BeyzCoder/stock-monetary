"""
This route handles the history prices of the stock.
- history price

Coded: Steven Baes
Date: 11 Jan, 2023
"""
import sys
import os

sys.path.append(os.getcwd())

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Union

from api.errors import http
from api.webscrape import request

# TODO: Place optional arguments.
# - range
# - interval
router = APIRouter()

@router.get("/history-price")
async def history_price(symbol: str = "", range: Union[str, None] = None) -> JSONResponse:
    # Prompt them a usage.
    if symbol == "": raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=http.BAD_REQUEST_PROMPT)

    query_parameters = {}
    if not range is None:
        query_parameters['range'] = range

    data = request.get_price(symbol, **query_parameters)
    if data == {}:
        # Insert the user's input for them to double check it quickly.
        detail = http.NOT_FOUND_PROMPT.copy()
        detail["Input"] = symbol
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    return JSONResponse(status_code=status.HTTP_200_OK, content=data, media_type="application/json")
