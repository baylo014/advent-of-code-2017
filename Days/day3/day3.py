import math
def part1(num):
    ring = math.ceil(((num**0.5) - 1)/2)
    npos = (num - (2*ring - 1)**2)%(2*ring)
    dist = abs(ring - npos)
    print(ring + dist)
def part2(num):
    print()

def main():
    '''
    part1(1)
    part1(12)
    part1(23)
    part1(1024)
    '''
    part1(312051)

    part2(5)
if __name__ == '__main__':
    main()
