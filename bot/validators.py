import re
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)

class InputValidator:
    @staticmethod
    def validate_symbol(symbol: str) -> Tuple[bool, Optional[str]]:
        pattern = r'^[A-Z]{2,10}USDT$'
        if not re.match(pattern, symbol.upper()):
            return False, "Symbol must be in format like BTCUSDT"
        return True, None
    
    @staticmethod
    def validate_side(side: str) -> Tuple[bool, Optional[str]]:
        if side.upper() not in ['BUY', 'SELL']:
            return False, "Side must be BUY or SELL"
        return True, None
    
    @staticmethod
    def validate_order_type(order_type: str) -> Tuple[bool, Optional[str]]:
        if order_type.upper() not in ['MARKET', 'LIMIT']:
            return False, "Order type must be MARKET or LIMIT"
        return True, None
    
    @staticmethod
    def validate_quantity(quantity: str) -> Tuple[bool, Optional[str], Optional[float]]:
        try:
            qty = float(quantity)
            if qty <= 0:
                return False, "Quantity must be > 0", None
            return True, None, qty
        except ValueError:
            return False, "Quantity must be a number", None
    
    @staticmethod
    def validate_price(price: str) -> Tuple[bool, Optional[str], Optional[float]]:
        try:
            p = float(price)
            if p <= 0:
                return False, "Price must be > 0", None
            return True, None, p
        except ValueError:
            return False, "Price must be a number", None
