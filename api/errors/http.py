from typing import Dict

BAD_REQUEST_PROMPT: Dict = {
    "Message" : "It requires a query parameter to be able to see the financial statement of a company.",
    "Usage" : "symbol=AAPL"
}

NOT_FOUND_PROMPT: Dict = {
    "Error" : "The argument was input does not exist from our source double check if the company have a different ticker symbol."
}