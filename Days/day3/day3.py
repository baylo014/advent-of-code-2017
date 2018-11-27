import math
from itertools import count

def part1(num):
    ring = math.ceil(((num**0.5) - 1)/2)
    npos = (num - (2*ring - 1)**2)%(2*ring)
    dist = abs(ring - npos)
    print(ring + dist)
# Assistance was found on being able to generate this specific stream
def sum_spiral():
    a, i, j = {(0,0) : 1}, 0, 0
    for s in count(1, 2):
        for (ds, di, dj) in [(0,1,0),(0,0,-1),(1,-1,0),(1,0,1)]:
            for _ in range(s+ds):
                i += di; j += dj
                a[i,j] = sum(a.get((k,l), 0) for k in range(i-1,i+2) for l in range(j-1,j+2))
                yield a[i,j]

def part2(n):
    for x in sum_spiral():
        if x>n: return x

def main():
    '''
    part1(1)
    part1(12)
    part1(23)
    part1(1024)
    '''
    part1(312051)

    print(part2(312051))
if __name__ == '__main__':
    main()
