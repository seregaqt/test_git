class Taxi:

    def __init__(self, traf, a, b):
        self.traf = traf
        self.a = a
        self.b = b

    def getTrafic(self):
        pass

    def getFunctions(self):
        pass


class Trafic(Taxi):

    def __init__(self, traf, a, b):
        super().__init__(traf, a, b)
        self.a = Taxi.a
        self.b = Taxi.b

    def getTrafic(self):
        if self.traf == 'Э':
            print('Эконом')
        if self.traf == 'К':
            print('Комфорт')

    def getFunctions(self):
        pass


class Functions(Trafic):

    def __init__(self, a, b, traf):
        super().__init__(traf, a, b)

    def getFunctions(self):

        if self.a == 1:
            print('С ребёнком')
        else:
            print('Без ребёнка')

        if self.b == 1:
            print('С багажом')
        else:
            print('Без багажа')
#
#
# def showTrafic(Taxi):
#     print(Taxi.getTrafic())
#
#
# def showFunctions(Trafic):
#     print(Trafic.getFunctions())


order_one = Taxi('Э', 0, 1)
order_two = Taxi('К', 1, 1)


# showTrafic(order_one)
# showTrafic(order_two)
