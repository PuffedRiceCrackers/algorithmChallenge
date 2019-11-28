def organizingContainers(containers):
    sumInContainer = [sum(container) for container in containers]
    sumInContainer.sort()
    sumOfBalls = [0 for container in containers]
    for i in range(len(containers)):
        for j in range(len(containers[i])):
            sumOfBalls[j] += containers[i][j]
    sumOfBalls.sort()
    return "Possible" if sumOfBalls == sumInContainer else "Impossible"