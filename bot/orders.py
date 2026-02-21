import logging
from typing import Dict, Optional, Tuple

logger = logging.getLogger(__name__)

class OrderManager:
    def __init__(self, client):
        self.client = client
    
    def place_market_order(self, symbol, side, quantity):
        try:
            response = self.client.place_order(symbol, side, 'MARKET', quantity)
            return True, "Order successful", response
        except Exception as e:
            return False, str(e), None
    
    def place_limit_order(self, symbol, side, quantity, price):
        try:
            response = self.client.place_order(symbol, side, 'LIMIT', quantity, price)
            return True, "Order successful", response
        except Exception as e:
            return False, str(e), None
