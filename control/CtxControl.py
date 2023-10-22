

class CtxControl:
    def __init__(self):
        self.__strategy__ = None

    def setStrategy(self, strtgy):
        self.__strategy__ = strtgy

    def search(self, a, b):
        self.__strategy__.searchFor(a, b)
