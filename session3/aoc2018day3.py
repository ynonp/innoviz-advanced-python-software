



# Coffee Break until 12:18
# Then we talk about Pandas




import re
import numpy as np

cloth = np.zeros(shape=(1_000, 1_000))


with open('day3.txt') as f:
    for line in f:
        m = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
        id, x, y, w, h, = [int(x) for x in m.groups()]
        cloth[x:x+w, y:y+h] += 1


print(np.count_nonzero(cloth > 1))


