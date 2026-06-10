def solution(s):
    answer = True
    stack = []
    for i in s:
        if len(stack) > 0 and stack[-1] == '(' and i ==')':
            stack.pop()
            continue
        stack.append(i)
    if len(stack) > 0:
        return False
    return True