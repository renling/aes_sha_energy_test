#!/usr/bin/python
from random import randint

def opt_cache_sim(N, C, M):
    reuse = [[] for _ in range(N)]
    S = [randint(0, N-1) for _ in range(M)]
    for i in range(M):
        reuse[S[i]].append(i)
    for i in range(N):
        reuse[i].append(M)

    cache = set()
    hit = miss = 0
    for i in range(M):
        x = S[i]
        reuse[x].pop(0)
        if x in cache:
            hit += 1
            continue
        miss += 1
        
        cache.add(x)
        if len(cache) <= C:
            continue
        evict = N
        for eline in cache:
            if evict == N:  
                evict = eline
            elif reuse[eline][0] > reuse[evict][0]:
                evict = eline
        cache.remove(evict)

    print(hit, miss)
        
    
 
C = 256   # cache size in lines
N = C * 128  # mem size in lines
M = N * 8    # sequence length

opt_cache_sim(N, C, M)


