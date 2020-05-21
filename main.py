#Суммирование значений цикла до тех пор, пока сумма чисел будет менее 1000
i = 0
sum = 0
while True:
    sum += i
    if sum >=1000:
        break
    print (sum)
    i += 1


#Выислить факториал числа

from math import factorial
i = int(input("Enter a:"))
s = factorial(i)
print(s)


#Вычислить площадь треугольника по 3 сторонам

from math import sqrt
a = int (input("Введите  длину первой стороны треугольника:"))
b = int (input("Введите  длину второй стороны треугольника:"))
c = int (input("Введите  длину третьей стороны треугольника"))
p = (a+b+c)/2
print("Площадь треугольника равна: ", sqrt(p*(p-a)*(p-b)*(p-c)))
