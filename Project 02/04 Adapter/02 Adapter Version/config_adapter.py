from abc import ABC, abstractclassmethod
from bs4 import BeautifulSoup
from typing import Any


class Config(ABC):

    @abstractclassmethod
    def get(self, key: str, default: Any = None):
        """Return the value associated with the key"""


class XMLConfig(Config):
    def __init__(self, bs: BeautifulSoup):
        self.bs = bs

    def get(self, key: str, default: Any = None):
        value = self.bs.find(key)
        if not value:
            return default
        return value.get_text()
