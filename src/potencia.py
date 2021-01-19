class Potencia:
    elementos = []
    exponente = 0

    def __init__(self, numero, exponente):
        self.__importarNumero(numero)
        self.exponente = exponente

    def __importarNumero(self, numero):
        self.elementos = [int(x) for x in str(numero)]

    def sumaPotencia(self):
        return sum( x ** self.exponente for x in self.elementos)
