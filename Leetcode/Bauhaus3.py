def solve(arr: list)->bool:
    s = set(arr)
    max_a = max(arr)
    min_a = min(arr)
    min_s = min(s)

    # max_s = max(s)
    # print(max_a,len(arr)-1, min_s, min_a)
    if len(s)==len(arr) and max_a == min_s+len(arr)-1 and min_a == min_s:
        return True
    else:
        return False

print(solve([5, 1, 4, 3, 2]))
print(solve([5, 1, 4, 3, 2, 8]))
print(solve([5, 6, 7, 8, 9, 9]))