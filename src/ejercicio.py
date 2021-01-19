class sumaCuadradosCubos:
    elements = []
    # El constructor almacena cada digito de la entrada
    def __init__(self, number):
        self.elements = [int(x) for x in str(number)]
        print(self.elements)

    def __sumaCuadrados(self):
        return sum( x ** 2 for x in self.elements)

    def __sumaCubos(self):
        return sum( x ** 3 for x in self.elements)

    def test(self):
        print(self.__sumaCuadrados())
        print(self.__sumaCubos())

a = sumaCuadradosCubos(333)
a.test()
