#Напишите такое лямбда-выражение transformation, чтобы transformed_values
#получился копией values. Переменная transformation должна быть глобальной,
#чтобы проверяющая система смогла его найти. Кроме transformation вам ничего
#писать не нужно. Печатать на экран – тоже.

transformation = lambda x: x

values = [1, 23, 42, "asdfg"]
transformed_values = list(map(transformation, values))
if values == transformed_values:
    print('ok')
else:
    print('fail')
