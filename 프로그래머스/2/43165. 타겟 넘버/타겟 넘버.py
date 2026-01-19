from collections import deque

def bfs(numbers, target):
    # (현재 인덱스, 현재까지의 합계)를 큐에 저장
    queue = deque([(0, 0)])
    count = 0
    n = len(numbers)
    while queue:
        i, s = queue.popleft()
        if i == n:
            if target == s:
                count += 1
        else:
            queue.append([i+1,s + numbers[i]])
            queue.append([i+1,s - numbers[i]])
    return count

def solution(numbers, target):
    return bfs(numbers, target)