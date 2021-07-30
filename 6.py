from itertools import count

for el in count(21):
    if el > 30:
        break
    else:
        print(el)

from itertools import cycle

с = 0
for el in cycle(str(1234)):
    if с > 10:
        break
    print(el)
    с += 1
