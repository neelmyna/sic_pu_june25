#!/bin/python3

def getMinimumCost(k, c): # k = 2
    c.sort() # 2 5 6
    i = 1
    j = 1
    minimum_cost = 0
    while i <= len(c): # 1 2 3
        if i <= k:
            minimum_cost += c[-i] # 6 + 5
        else:
            minimum_cost += (j + 1) * c[-i]
            if i % k == 0:
                j += 1
        i += 1
    return minimum_cost

if __name__ == '__main__':
    nk = input('Enter space seperated values for N and K: ').split()
    n = int(nk[0])
    k = int(nk[1])
    print('Enter cost of the flowers:')
    c = list(map(int, input().rstrip().split()))
    minimumCost = getMinimumCost(k, c)
    print(f'Minimum Cost = {minimumCost}')