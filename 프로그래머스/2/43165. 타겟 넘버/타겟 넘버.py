from collections import deque

def dfs(numbers,target):
    queue = deque([(0, 0)])
    count = 0
    n = len(numbers)
    while queue:
        i, s = queue.pop()
        if i == n:
            if target == s:
                count += 1
        else:
            queue.append([i+1,s + numbers[i]])
            queue.append([i+1,s - numbers[i]])
    return count
def solution(numbers, target):
    return dfs(numbers, target)