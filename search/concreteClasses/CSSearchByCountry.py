from display.Display import Display
from search.IStrategy import IStrategy


class CSSearchByCountry(IStrategy):
    def searchFor(self, a, b):
        display = Display()
        display.showByCountry(b)