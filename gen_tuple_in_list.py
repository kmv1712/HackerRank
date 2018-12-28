"""из вида  
x = [1, 2]
y = [3, 4]
получаем
(1, 3) (1, 4) (2, 3) (2, 4)


# Интересное решение
from itertools import product

a = list(map(int, input().split()))
b = list(map(int, input().split()))
развертываем к конечному виду (1, 3) (1, 4) (2, 3) (2, 4)
print(*product(a, b))

# Мое решение
x = input()
y = input()
x = x.split()
y = y.split()
new = []
# Генерирует значение вида <class 'list'>: [(1, 3), (1, 4), (2, 3), (2, 4)] аналог product()
z = ((int(i), int(j)) for i in x for j in y)
q = list(z)
<------------------> # можно заменить на print(*q)
for item in q:
    w = str(item)
    new.append(w)  

print(" ".join(new))
