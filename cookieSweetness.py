def func():
    pass

import heapq

def cookies(k, A):
    heapq.heapify(A)
    n = 0

    while True:
        a = heapq.heappop(A)
        if a >= k:
            return n
        if not A:
            return -1
        
        b = heapq.heappop(A)
        heapq.heappush(A, a + 2 * b)
        n += 1



if __name__ == "__main__":
    print('We have new routines')
    '''
    H = [21, 1, 45, 78, 3, 5]

    heapq.heapify(H)
    print(H)
    while H:
        print(heapq.heappop(H))
        print(H)
        '''

    k = 9
    AA = [2, 7, 3, 6, 4, 6]

    print(cookies(k, AA))

    k = 7
    AA = [1, 2, 3, 9, 10, 12]

    print(cookies(k, AA))