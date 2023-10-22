from abc import ABC, abstractmethod
import json


class Display:

    def showByName(self, b):
        with open('data.json') as f:
            data = json.load(f)
            for university in data:
                if b == university["name"]:
                    programmes = university["programmes"]
                    print(f'''
        Name: {university["name"]}
        Country: {university["country"]}
        City: {university["city"]}
        Programmes:                    ''')
                    for ps in programmes:
                        print("     - " + ps)

    def showByCountry(self, b):
        with open('data.json') as f:
            data = json.load(f)
            for countries in data:
                if b == countries["country"]:
                    print(countries["name"])

    def showByCourse(self, b):
        with open('data.json') as f:
            data = json.load(f)
            print("Essas universidades oferecem o curso de " + b + ":")
            for elements in data:
                length = len(elements["programmes"])
                for j in range(0, length):
                    if elements["programmes"][j] == b:
                        print("  -" + elements["name"])




class IStrategy(ABC):

    @abstractmethod
    def searchFor(self, a, b):
        pass


class CSSearchByUni(IStrategy):
    def searchFor(self, a, b):
        display = Display()
        display.showByName(b)


class CSSearchByCourse(IStrategy):
    def searchFor(self, a, b):
        display = Display()
        display.showByCourse(b)


class CSSearchByCountry(IStrategy):
    def searchFor(self, a, b):
        display = Display()
        display.showByCountry(b)


class CtxControl:
    def __init__(self):
        self.__strategy__ = None

    def setStrategy(self, strtgy):
        self.__strategy__ = strtgy

    def search(self, a, b):
        self.__strategy__.searchFor(a, b)


control = CtxControl()
while True:

    code = input('''
                 Como realizar a busca?
                 A: Buscar pelo nome da unviersidade
                 B: Buscar pelo país
                 C: Buscar pelo curso
                 ''')
    name = input('O que buscar? Digite o texto...')

    if code == 'A' or code == 'a':
        control.setStrategy(CSSearchByUni())
        control.search(code, name)
    elif code == 'B' or code == 'b':
        control.setStrategy(CSSearchByCountry())
        control.search(code, name)
    elif code == 'C' or code == 'c':
        control.setStrategy(CSSearchByCourse())
        control.search(code, name)
    else:
        print('não encontrado')
