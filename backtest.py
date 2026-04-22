import ccxt

def backtest():
    exchange = ccxt.binance()
    data = exchange.fetch_ohlcv('BTC/USDT', timeframe='1m', limit=100)

    balance = 1000

    for candle in data:
        close = candle[4]

        if close % 2 == 0:
            balance += 3
        else:
            balance -= 1

    print("Final bakiye:", balance)