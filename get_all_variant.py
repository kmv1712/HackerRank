#Интересный вариант

from itertools import permutations
s,n = input().split()
print(*[''.join(i) for i in permutations(sorted(s),int(n))],sep='\n')

#Мой вариант
from itertools import permutations
user, dig = input().split()
for item in sorted(list(permutations(user, int(dig)))):
    print(''.join(list(item)))
