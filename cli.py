import os
import sys
import logging
from bot.client import BinanceFuturesClient
from bot.orders import OrderManager
from bot.validators import InputValidator
from bot.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    print("\n" + "="*50)
    print("BINANCE FUTURES TRADING BOT")
    print("="*50)
    
    client = BinanceFuturesClient()
    validator = InputValidator()
    order_manager = OrderManager(client)
    
    while True:
        print("\n--- Enter Order Details ---")
        
        # Get symbol
        while True:
            symbol = input("Symbol (BTCUSDT/ETHUSDT): ").strip().upper()
            valid, error = validator.validate_symbol(symbol)
            if valid:
                break
            print(f"Error: {error}")
        
        # Get side
        while True:
            side = input("Side (BUY/SELL): ").strip().upper()
            valid, error = validator.validate_side(side)
            if valid:
                break
            print(f"Error: {error}")
        
        # Get order type
        while True:
            order_type = input("Order Type (MARKET/LIMIT): ").strip().upper()
            valid, error = validator.validate_order_type(order_type)
            if valid:
                break
            print(f"Error: {error}")
        
        # Get quantity
        while True:
            qty_str = input("Quantity: ").strip()
            valid, error, quantity = validator.validate_quantity(qty_str)
            if valid:
                break
            print(f"Error: {error}")
        
        # Get price for limit orders
        price = None
        if order_type == 'LIMIT':
            while True:
                price_str = input("Price: ").strip()
                valid, error, price = validator.validate_price(price_str)
                if valid:
                    break
                print(f"Error: {error}")
        
        # Confirm order
        print(f"\nOrder Summary:")
        print(f"  Symbol: {symbol}")
        print(f"  Side: {side}")
        print(f"  Type: {order_type}")
        print(f"  Quantity: {quantity}")
        if price:
            print(f"  Price: {price}")
        
        confirm = input("\nConfirm? (yes/no): ").strip().lower()
        if confirm not in ['yes', 'y']:
            print("Order cancelled")
            continue
        
        # Place order
        if order_type == 'MARKET':
            success, message, details = order_manager.place_market_order(symbol, side, quantity)
        else:
            success, message, details = order_manager.place_limit_order(symbol, side, quantity, price)
        
        if success:
            print(f"\n✅ SUCCESS: {message}")
            if details:
                print(f"  Order ID: {details.get('orderId')}")
                print(f"  Status: {details.get('status')}")
                if details.get('avgPrice'):
                    print(f"  Avg Price: {details.get('avgPrice')}")
        else:
            print(f"\n❌ FAILED: {message}")
        
        # Another order?
        another = input("\nAnother order? (yes/no): ").strip().lower()
        if another not in ['yes', 'y']:
            break
    
    print("\nThank you for using the bot!")

if __name__ == '__main__':
    main()
