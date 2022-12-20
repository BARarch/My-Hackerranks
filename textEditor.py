def query(state, cmd, st=''):
    if cmd == "1":
        state.append(state[-1] + st)
    elif cmd == "2":
        state.append(state[-1][:-int(st)])
    elif cmd == "3":
        #print(f'state:{state} k:{st}')
        print(state[-1][int(st) - 1])
    elif cmd == "4":
        if len(state) > 1:
            state.pop()
    #print(f'cmd:{cmd} input:{st} {state}')


if __name__ == "__main__":
    from collections import deque
    state = ['',]
    N = int(input())
    
    for _ in range(N):
        query(state, *input().rsplit())