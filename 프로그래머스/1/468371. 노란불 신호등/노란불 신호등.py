def solution(signals):
    answer = -1
    for time in range(1, 9999999):
        all_yellow = True
        for g, y, r in signals:
            cycle = g + y + r
            t = time % cycle
            if t == 0:
                t = cycle
            if not (g < t <= g + y):
                all_yellow = False
                break
                
        if all_yellow:
            answer = time
            break
            
    return answer