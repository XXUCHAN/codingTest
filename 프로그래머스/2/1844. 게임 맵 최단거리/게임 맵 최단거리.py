from collections import deque
def dfs(maps,n,m):
    visited = set([(0,0)])
    need_visited = deque([(0,0,1)])
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    while need_visited:
        x,y,dist = need_visited.popleft()
        if x == m - 1 and y == n - 1:
            return dist
        for dx,dy in delta:
            newX = dx + x
            newY = dy + y
            if newX >= 0 and newX < m and newY>=0 and newY <n:
                if maps[newY][newX] == 1 and (newX,newY) not in visited:
                    visited.add((newX,newY))
                    need_visited.append((newX,newY,dist + 1))
    return -1
def solution(maps):
    n = len(maps)
    m = len(maps[0])
    return dfs(maps,n,m)