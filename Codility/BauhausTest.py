def solution2(A):
    # write your code in Python 3.6
    n = len(A)
    ans = 0
    summ = 0
    repo = list()
    for i in range(n):
        summ += A[i]
        repo.append(A[i])
        if summ < 0:
            ans += 1
            mi = min(repo)
            summ = summ - mi
            print(repo, mi)
            repo.remove(mi)
    return ans
res = solution2([-1,2, -2,1,  -3, 3])
print(res)

def solution3(A, K):
    n = len(A)
    for i in range(n - 1):
        if (A[i] + 1 < A[i + 1]):
            return False
    if (A[0] != 1 or A[n - 1] != K):
        return False
    else:
        return True
res = solution3([1, 2, 3, 4], 3)
print(res)

def solution1(s):
    c = s[0]
    if c.isalpha() and c == c.upper():    # please fix condition
        return "upper"
    elif c.isalpha() and c == c.lower():  # please fix condition
        return "lower"
    elif c.isdigit():  # please fix condition
        return "digit"
    else:
        return "other"
res = solution1('abc')
print(res)

