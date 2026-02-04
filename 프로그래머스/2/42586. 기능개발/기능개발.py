import math

def solution(progresses, speeds):
    answer = []
    # 예: [93, 30, 55], [1, 30, 5] -> [7, 3, 9]
    days = [math.ceil((100 - p) / s) for p, s in zip(progresses, speeds)]
    
    front = 0 # 배포 기준이 되는 앞선 작업의 인덱스
    for i in range(len(days)):
        # 현재 작업이 기준 작업보다 늦게 끝나면, 지금까지 쌓인 작업을 배포합니다.
        if days[i] > days[front]:
            answer.append(i - front)
            front = i # 기준을 현재 작업으로 변경
            
    # 마지막으로 남은 작업들을 배포합니다.
    answer.append(len(days) - front)
    
    return answer