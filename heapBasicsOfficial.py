import os
import math
import heapq

if __name__ == "__main__":
    N = int(input())
    H = []
    D = []
    heapq.heapify(H)
    heapq.heapify(D)
     
    for _ in range(N):
        q = input().split()
        if q[0] == "1":
            heapq.heappush(H, int(q[1]))
        elif q[0] == "2":
            heapq.heappush(D, int(q[1]))
        elif q[0] == "3":
            while D and H[0] == D[0]:
                heapq.heappop(D)
                heapq.heappop(H)
            print(H[0])
           