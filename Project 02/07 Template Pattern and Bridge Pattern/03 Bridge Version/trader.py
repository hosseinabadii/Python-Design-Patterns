from typing import List
from abc import ABC, abstractclassmethod
from exchange import Exchange


class Trader(ABC):
    def __init__(self, exchange: Exchange):
        self.exchange = exchange

    def list_average(self, l: List[float]) -> float:
        return sum(l) / len(l)
        
    def check_prices(self, coin: str):
        self.exchange.connect()
        prices = self.exchange.get_market_data(coin)
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


class MinMaxTrader(Trader):
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] == min(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] == max(prices)


class AverageTrader(Trader):
    def should_buy(self, prices: List[float]) -> bool:
        return prices[-1] < self.list_average(prices)

    def should_sell(self, prices: List[float]) -> bool:
        return prices[-1] > self.list_average(prices)
