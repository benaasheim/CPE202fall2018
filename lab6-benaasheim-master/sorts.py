import random
import time

def selection_sort(lis):
    placemark = 0
    comps = 0
    lowest = lis[0]
    lowin = 0
    while placemark < len(lis):
        lowest = lis[placemark]
        lowin = placemark
        for s in range(lowin, len(lis)):
            if lis[s] < lowest:
                comps += 1
                lowest = lis[s]
                lowin = s
        print(placemark, lis[placemark])
        a = lis[placemark]
        lis[placemark] = lowest
        lis[lowin] = a
        placemark += 1
        print(lis)
    return comps

def insertion_sort(lis):
    comps = 0
    n = 1
    placemark = 1
    while placemark < len(lis):
        print(placemark, lis)
        if (n > 0) and (lis[n] < lis[n-1]):
            comps += 1
            a = lis[n]
            lis[n] = lis[n-1]
            lis[n-1] = a
            n -= 1
        else:
            n = placemark
            placemark += 1
    return comps


def main():
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time()
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__':
    main()
