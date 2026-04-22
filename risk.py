import config

def check_risk(balance):
    if balance < config.MIN_BALANCE:
        return False
    if balance > config.MAX_TRADE_USDT:
        return False
    return True