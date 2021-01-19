from potencia import Potencia
class SumaCuadrados(Potencia):
    def __init__(self, numero):
        Potencia.__init__(self, numero, 2)

a = SumaCuadrados(123)
print(a.elementos)
print(a.exponente)
print(a.sumaPotencia())
