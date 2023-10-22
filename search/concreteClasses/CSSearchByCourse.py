from display.Display import Display
from search.IStrategy import IStrategy


class CSSearchByCourse(IStrategy):
    def searchFor(self, a, b):
        display = Display()
        display.showByCourse(b)

