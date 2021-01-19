from potencia import Potencia
class SumaCubos(Potencia):
    def __init__(self, numero):
        Potencia.__init__(self, numero, 3)

a = SumaCubos(123)
print(a.elementos)
print(a.exponente)
print(a.sumaPotencia())
