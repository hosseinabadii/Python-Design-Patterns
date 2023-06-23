from typing import List
from abc import ABC, abstractclassmethod

class TradingBot(ABC):

    def connect(self):
        print(f"Connecting to Crypto Exchange...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 16, 20, 90]
    
    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)
        
    def check_prices(self, coin: str):
        self.connect()
        prices = self.get_market_data(coin)
        should_buy = self.should_buy(prices)
        should_sell = self.should_sell(prices)
        if should_buy:
            print(f"You should buy {coin}")
        elif should_sell:
            print(f"You should sell {coin}")
        else:
            print(f"No action needed for {coin}")

    @abstractclassmethod
    def should_buy(self, prices: List[float]) -> bool:
        pass

    @abstractclassmethod
    def should_sell(self, prices: List[float]) -> bool:
        pass


class MinMaxTrader(TradingBot):
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)


class AverageTrader(TradingBot):
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)

app = MinMaxTrader()
app.check_prices("BTC/USD")