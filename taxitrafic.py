class Taxi:

    def __init__(self, traf,a,b):
        self.traf = traf
        self.a = a
        self.b = b

    def getTrafic(self):
        pass

    def getFunctions(self):
        pass

class Trafic(Taxi):

    def __init__(self, traf):
        self.traf = traf

    def getTrafic(self):
        if self.traf == 'Э':
            print('Эконом')
        if self.traf == 'К':
            print('Комфорт')

    def getFunctions(self):
        pass

class Functions(Trafic):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def getFunctions(self):
        if self.a == 1:
            print('С ребёнком')
        else:
            print('Без ребёнка')

        if self.b == 1:
            print('С багажом')
        else:
            print('Без багажа')

def showTrafic(Taxi):
    print(Taxi.getTrafic())

def showFunctions(Trafic):
    print(Trafic.getFunctions())



order_one = Taxi('Э', 0, 0)
order_two = Taxi('К', 1, 1)

showTrafic(order_one)
showTrafic(order_two)

