def solution(sizes):
    for size in sizes:
        size.sort(reverse=True)
    w,h = map(list,zip(*sizes))
    print(w,h)
    return max(w) * max(h)
