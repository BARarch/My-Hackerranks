def avoidObstacles(inputArray):
    jump = 2

    while jump <= max(inputArray):
        #print("jump " + str(jump))
        tripped = False
        for obstacle in inputArray:
            if (obstacle % jump) == 0:
                #print("Tripped on " + str(obstacle))
                tripped = True
                jump += 1

                break
        
        if not tripped:
            break

    return jump

