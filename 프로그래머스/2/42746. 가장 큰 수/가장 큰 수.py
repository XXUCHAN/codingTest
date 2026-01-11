from functools import cmp_to_key
def solution(numbers):
    largest_order = sorted(numbers, key=cmp_to_key(compare))
    result = "".join(map(str,largest_order))    
    if sum(largest_order) == 0:
        return "0"
    return result

def compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    else:
        return 1