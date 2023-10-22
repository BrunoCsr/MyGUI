from display.Display import Display
from search.IStrategy import IStrategy


class CSSearchByUni(IStrategy):
    def searchFor(self, a, b):
        display = Display()
        display.showByName(b)
