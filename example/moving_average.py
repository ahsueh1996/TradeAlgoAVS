import ccxt
import pandas as pd
import time

# Initialize exchange
exchange = ccxt.binance({
    'apiKey': 'YOUR_API_KEY',
    'secret': 'YOUR_SECRET_KEY',
})

symbol = 'BTC/USDT'
timeframe = '1h'
short_window = 9
long_window = 21

def fetch_data():
    """Fetch historical OHLCV data."""
    ohlcv = exchange.fetch_ohlcv(symbol, timeframe)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms')
    return df

def calculate_signals(df):
    """Generate trading signals based on moving average crossover."""
    df['SMA_short'] = df['close'].rolling(window=short_window).mean()
    df['SMA_long'] = df['close'].rolling(window=long_window).mean()
    df['signal'] = df['SMA_short'] > df['SMA_long']
    return df

def place_order(side, amount=0.001):
    """Place a market order."""
    try:
        order = exchange.create_market_order(symbol, side, amount)
        print(f"Order placed: {side} {amount} {symbol}")
    except Exception as e:
        print(f"Order failed: {e}")

def trading_bot():
    """Main trading loop."""
    last_signal = None
    while True:
        df = fetch_data()
        df = calculate_signals(df)
        current_signal = df['signal'].iloc[-1]
        
        if last_signal is not None:
            if current_signal and not last_signal:
                place_order('buy')
            elif not current_signal and last_signal:
                place_order('sell')
        
        last_signal = current_signal
        time.sleep(60)  # Sleep for 1 minute before checking again

if __name__ == "__main__":
    trading_bot()
