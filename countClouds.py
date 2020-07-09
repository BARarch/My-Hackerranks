#!/Users/anthonyquivers/anaconda3/bin/python
#Date Started: 190927

def neighbors_of_cloud(position):
    yield (position[0], position[1] + 1)
    yield (position[0] + 1, position[1])
    yield (position[0], position[1] - 1)
    yield (position[0] - 1, position[1])

def countClouds(skyMap):
    cloud = {}
    for i, row in enumerate(skyMap):
        for j, val in enumerate(row):
            if val == "1":
                cloud[(i, j)] = ''

    #print(cloud)
    #print(len(cloud))
    from collections import deque
    cloudInProgress = deque()
    n = 0
    while cloud:
        n += 1     
        cloudInProgress.append(next(iter(cloud)))
        cloud.pop(next(iter(cloud)))
        while cloudInProgress:
            pos = cloudInProgress.pop()
            for neighbor in neighbors_of_cloud(pos):
                if neighbor in cloud:
                    cloudInProgress.append(neighbor)
                    cloud.pop(neighbor)

    return n


if __name__ == '__main__':
    import os
    from cs_utils import *
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sky = list_string_to_list(input())

    print("input: {}".format(sky))


    fptr.write(str(countClouds(sky)))
    fptr.write('\n')

    fptr.close()