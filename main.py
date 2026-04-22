import asyncio
from async_bot import run_bot
from triangular import run_triangular
from backtest import backtest

print("1: Arbitraj Bot")
print("2: Triangular")
print("3: Backtest")

secim = input("Seçim: ")

if secim == "1":
    asyncio.run(run_bot())
elif secim == "2":
    run_triangular()
elif secim == "3":
    backtest()