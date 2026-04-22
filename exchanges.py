import ccxt  

def get_binance():
    return ccxt.binance({
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })

def get_kucoin():
    return ccxt.kucoin({
        'enableRateLimit': True,
        'options': {'defaultType': 'spot'}
    })