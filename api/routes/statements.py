"""
This route handles the financial statement of the stock.
- income statement
- balance statement
- cash statement

Coded: Steven Baes
Date: 03 Jan, 2023
"""
import sys
import os

sys.path.append(os.getcwd())

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from typing import Optional

from config import Statement
from api.errors import http
from api.webscrape import request

# TODO: Place a optional arguments.
# - frequency (Annually | Quarterly)
# - placeholder format 
router = APIRouter()

@router.get("/income")
async def income_statement(symbol: str = "", freq: Optional[str] = "A", formstyle: Optional[str] = "default") -> JSONResponse:
    # Prompt them a usage.
    if symbol == "": raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=http.BAD_REQUEST_PROMPT)

    data = request.get_statement(symbol, Statement.URL_INCOME_STATEMENT.value, freq, formstyle)
    if data == {}: 
        # Insert the user's input for them to double check it quickly.
        detail = http.NOT_FOUND_PROMPT.copy()
        detail["Input"] = symbol
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    return JSONResponse(status_code=status.HTTP_200_OK, content=data, media_type="application/json")

@router.get("/balance")
async def balance_statement(symbol: str = "", freq: Optional[str] = "A", formstyle: Optional[str] = "default") -> JSONResponse:
    # Prompt them a usage.
    if symbol == "": raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=http.BAD_REQUEST_PROMPT)
    
    data = request.get_statement(symbol, Statement.URL_BALANCE_STATEMENT.value, freq, formstyle)
    if data == {}: 
        # Insert the user's input for them to double check it quickly.
        detail = http.NOT_FOUND_PROMPT.copy()
        detail["Input"] = symbol
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    return JSONResponse(status_code=status.HTTP_200_OK, content=data, media_type="application/json")

@router.get("/cash")
async def cash_statement(symbol: str = "", freq: Optional[str] = "A", formstyle: Optional[str] = "default") -> JSONResponse:
    # Prompt them a usage.
    if symbol == "": raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=http.BAD_REQUEST_PROMPT)
    
    data = request.get_statement(symbol, Statement.URL_CASH_STATEMENT.value, freq, formstyle)
    if data == {}: 
        # Insert the user's input for them to double check it quickly.
        detail = http.NOT_FOUND_PROMPT.copy()
        detail["Input"] = symbol
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

    return JSONResponse(status_code=status.HTTP_200_OK, content=data, media_type="application/json")
