if __name__ == '__main__':
    N = int(input())
    tt = []
    for _ in range(N):
        cmd = input().split(' ')
        if cmd[0] == 'insert':
            tt.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'print':
            print(tt)
        elif cmd[0] == 'remove':
            tt.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            tt.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            tt.sort()
        elif cmd[0] == 'pop':
            tt.pop()
        elif cmd[0] == 'reverse':
            tt.reverse()
