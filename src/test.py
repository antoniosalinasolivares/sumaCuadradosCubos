import random
from sumaCuadradosCubos import SumaCuadradosCubos


# pruebas con 20 numeros aleatorios
test_list = [random.randint(100, 999) for x in range(20)]
for item in test_list:
    print(SumaCuadradosCubos(item).resolver())


# pruebas con los valores predefinidos
print(SumaCuadradosCubos(589).resolver())
print(SumaCuadradosCubos(123).resolver())
