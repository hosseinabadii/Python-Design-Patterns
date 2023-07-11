from exchange import Exchange, BinanceExchange, CoinbaseExchange
from trader import Trader, MinMaxTrader, AverageTrader

def main(exchange: Exchange, trader: Trader):
    
    app = trader(exchange)
    app.check_prices("BTC/USD")


if __name__ == "__main__":
    exchange = BinanceExchange()
    trader = MinMaxTrader
    main(exchange, trader)