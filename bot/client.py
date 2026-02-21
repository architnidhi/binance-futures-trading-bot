import logging
import random
import time

logger = logging.getLogger(__name__)

class BinanceFuturesClient:
    def __init__(self, api_key=None, api_secret=None):
        logger.info("Initializing Mock Binance Client")
        self.order_counter = 1000
    
    def test_connection(self):
        logger.info("Testing connection...")
        time.sleep(0.5)
        return True
    
    def place_order(self, symbol, side, order_type, quantity, price=None):
        self.order_counter += 1
        
        if order_type.upper() == 'MARKET':
            status = 'FILLED'
            avg_price = random.uniform(50000, 51000)
            executed_qty = quantity
        else:
            status = 'NEW'
            avg_price = None
            executed_qty = 0
        
        response = {
            'orderId': self.order_counter,
            'symbol': symbol.upper(),
            'status': status,
            'executedQty': str(executed_qty),
            'avgPrice': str(avg_price) if avg_price else None,
            'price': str(price) if price else None,
            'origQty': str(quantity),
            'side': side.upper(),
            'type': order_type.upper()
        }
        
        logger.info(f"Order placed: {response}")
        return response
