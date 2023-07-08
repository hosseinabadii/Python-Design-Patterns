from typing import List
from abc import ABC, abstractclassmethod


class Exchange(ABC):

    @abstractclassmethod
    def connect(self):
        pass

    @abstractclassmethod
    def get_market_data(self, coin: str) -> List[float]:
        pass
    

class BinanceExchange(Exchange):

    def connect(self):
        print("Connecting to Binance...")

    def get_market_data(self, coin: str) -> List[float]:
        return [10, 15, 20, 14]


class CoinbaseExchange(Exchange):

    def connect(self):
        print("Connecting to Coinbase...")

    def get_market_data(self, coin: str) -> List[float]:
        return [9, 12, 15, 11]
