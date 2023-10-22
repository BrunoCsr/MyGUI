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





