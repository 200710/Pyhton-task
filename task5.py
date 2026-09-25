def searcher(n):
    all = [True] * (n + 1)

    all[0] = all[1] = False
    
    for i in range(2, int(n**0.5) + 1):
        if all[i]:
            for j in range(i * i, n + 1, i):
                all[j] = False

    simple = [i for i in range(2, n + 1) if all[i]]
    return simple

print(searcher(1000))
