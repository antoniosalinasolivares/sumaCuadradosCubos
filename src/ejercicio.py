class sumaCuadradosCubos:
    elements = []
    # El constructor almacena cada digito de la entrada
    def __init__(self, numero):
        self.__importarNumero(numero)

    def __sumaCuadrados(self):
        return sum( x ** 2 for x in self.elements)

    def __sumaCubos(self):
        return sum( x ** 3 for x in self.elements)

    def resolver(self):
        return self.__sumaCuadrados() + self.__sumaCubos()

    def __importarNumero(self, numero):
        self.elements = [int(x) for x in str(numero)]

    def test(self):
        print(self.__sumaCuadrados())
        print(self.__sumaCubos())

a = sumaCuadradosCubos(589)
a.test()
print(a.resolver())
