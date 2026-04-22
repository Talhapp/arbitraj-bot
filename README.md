# arbitraj-bot
# 🤖 Cryptocurrency Arbitrage Trading Bot

An automated cryptocurrency arbitrage trading bot designed to identify and exploit price inefficiencies across trading pairs. The system continuously monitors market data, detects profitable opportunities, and executes trades in real-time.

## 🚀 Features

- Triangular Arbitrage Strategy
- Real-time market data monitoring
- Automated trade execution
- Logging system for all transactions
- HTTP-based notification module
- Backtesting support for strategy validation
- Configurable trading parameters

## 🧠 Core Logic

The bot focuses on **triangular arbitrage**, which involves exploiting price differences between three trading pairs within the same exchange.

Example cycle:
BTC → ETH → USDT → BTC

The system:
- Fetches live market data via exchange APIs
- Calculates cross exchange rates
- Detects arbitrage opportunities after fees
- Executes sequential trades automatically
- Logs every transaction step

## 🛠️ Tech Stack

- Python
- REST APIs (Exchange integration)
- Requests library
- JSON handling
- File-based logging system
- Modular architecture

## 📂 Project Structure

/project
│
├── main.py          # Core bot execution loop  
├── logger.py        # Trade logging system  
├── notifier.py      # Notification handler  
├── config.py        # API keys and settings  
└── trades.log       # Trade history logs  

## ⚙️ Workflow

1. Collect real-time market prices from exchanges  
2. Generate possible triangular arbitrage paths  
3. Calculate potential profit after fees  
4. Filter profitable opportunities  
5. Execute buy/sell orders automatically  
6. Log results and send notifications  

## 📊 Backtesting

The bot includes a backtesting module to:
- Simulate historical market conditions  
- Evaluate strategy performance  
- Optimize trading parameters  
- Reduce real-market risk  

## 🔐 Security

- API keys stored in `config.py`
- Sensitive files excluded via `.gitignore`
- Recommended use of restricted exchange API permissions

## ⚠️ Disclaimer

This project is intended for educational and research purposes only. Cryptocurrency trading involves financial risk. The developer is not responsible for any financial losses.

## 👨‍💻 Author

Talha Puşuroğlu  
Computer Programming Student

## 📌 Future Improvements

- Multi-exchange support  
- WebSocket-based low latency data feed  
- Advanced risk management system  
- Real-time dashboard UI  
- Machine learning-based opportunity detection  
