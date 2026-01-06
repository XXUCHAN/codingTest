from collections import Counter
def solution(participant, completion):
    participantCounter = Counter(participant)
    for p in completion:
        participantCounter[p] -= 1
    return participantCounter.most_common(1)[0][0]