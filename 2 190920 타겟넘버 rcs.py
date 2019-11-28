def solution(numbers, target):
    if len(numbers) == 1:
        if target == numbers[0] or target == (-numbers[0]):
            return 1
        else:
            return 0
    else:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])

numbers = [1,1,1]
target = 1
print(solution(numbers, target))