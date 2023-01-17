"""
TODO
"""
import sys
import os

sys.path.append(os.getcwd())

from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse

from api.errors import http
from api.webscrape import request