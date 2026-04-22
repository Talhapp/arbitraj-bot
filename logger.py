def log_trade(msg):
    print("LOGGER INPUT:", type(msg), msg)

    with open("trades.log", "a") as f:
        f.write(str(msg) + "\n")