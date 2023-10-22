
from control.CtxControl import CtxControl
from search.concreteClasses.CSSearchByCountry import CSSearchByCountry
from search.concreteClasses.CSSearchByCourse import CSSearchByCourse
from search.concreteClasses.CSSearchByUni import CSSearchByUni

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
