def power_set(S):
    print(f'power set: {S}')
    if len(S) == 0:
        yield set([])
    else:
        a = S.pop()
        acc = []
        for s in power_set(S):
            yield s
            acc.append(s)
        #print(acc)
        for b in acc:
            yield b.union(set([a]))


if __name__ == "__main__":
    for r in power_set(set(['a', 'b', 'c', 'd'])):
        print(r)
