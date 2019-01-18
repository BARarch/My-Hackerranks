from collections import deque

if __name__ == '__main__':
    for test in range(int(input().rstrip())):
        n = int(input().rstrip())
        cubes = deque(list(map(int, input().rstrip().split(' '))))
        if len(cubes) == 1:
            print("Yes")
            continue

        status = None
        left = cubes.popleft()
        right = cubes.pop()
        last = 2 << 31
        while cubes:
            if left >= right:
                # Use left
                if left <= last:
                    last = left
                    left = cubes.popleft()
                else:
                    status = 'No'
                    break
            else:
                # Use right
                if right <= last:
                    last = right
                    right = cubes.pop()
                else:
                    status = 'No'
                    break

        # cubes deque empty Final Stage
        if not status:
            status = "No"
            if left >= right:
                if left <= last:
                    status = "Yes"
            else:
                if right <= last:
                    status = "Yes"
        
        print(status)
