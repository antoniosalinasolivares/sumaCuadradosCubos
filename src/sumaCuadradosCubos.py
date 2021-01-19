from sumaCubos import SumaCubos
from sumaCuadrados import SumaCuadrados

class SumaCuadradosCubos:

    cuadrados = None
    cubos = None

    def __init__(self, numero):
        if(self.__validarEntrada(numero)):
            numero = int(numero)
        self.cuadrados = SumaCuadrados(numero)
        self.cubos = SumaCubos(numero)

    def resolver(self):
        return self.cuadrados.sumaPotencia() + self.cubos.sumaPotencia()

    def __validarEntrada(self, numero):
        if(not isinstance(numero, int)):
            print('los valores de entrada debe ser un numero entero, \nEs posible que encuentres errores de ejecucion')
            return True
        return False

