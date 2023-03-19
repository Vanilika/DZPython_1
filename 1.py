# Задача 2: Найдите сумму цифр трехзначного числа.

Number = int (input('Введите число: '))
summa = 0
if 100 <= Number < 1000:
    x = Number % 10
    y = Number % 100 / 10
    import math
    y = math.floor(y)
    z = Number % 1000 / 100 
    import math
    z  = math.floor(z)
    summa =  x + z + y
    print ("Сумма чисел =")
    print (summa)
    
    
else:
    print ("Число не трехзначное")