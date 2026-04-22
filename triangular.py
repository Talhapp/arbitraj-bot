import ccxt

def run_triangular():
    exchange = ccxt.binance()

    btc_usdt = exchange.fetch_ticker('BTC/USDT')['last']
    eth_usdt = exchange.fetch_ticker('ETH/USDT')['last']
    eth_btc = exchange.fetch_ticker('ETH/BTC')['last']

    btc = 1

    eth = btc / eth_btc
    usdt = eth * eth_usdt
    final_btc = usdt / btc_usdt

    print("Başlangıç:", btc)
    print("Son:", final_btc)

    if final_btc > btc:
        print("KAR VAR")
    else:
        print("KAR YOK")