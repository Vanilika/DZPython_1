# Задача 8: Требуется определить, 
# можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).

LengthChocolate = int(input("Введите количество долек шоколадки в длину:"))
WidthChocolate = int(input("Введите количество долек шоколадки в ширину:"))
HowManySliceBreakOff = int(input("Введите количество сколько долек шоколадки отломить:"))

if HowManySliceBreakOff % LengthChocolate == 0 or HowManySliceBreakOff % WidthChocolate == 0:
    print("Шоколад делится")
else:
    print("Шоколад не делится") 