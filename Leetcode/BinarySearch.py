from bisect import bisect_left


def my_bisect1(arr, k):
    lp, rp = 0, len(arr) - 1
    while lp <= rp:
        m = (lp + rp) // 2
        if arr[m] > k:
            rp = m - 1
        else:
            lp = m + 1
    return lp  # rp


def my_bisect2(arr, k):
    lp, rp = 0, len(arr) - 1
    while lp < rp:
        m = (lp + rp) // 2
        if arr[m] > k:
            rp = m
        else:
            lp = m + 1
    return lp


def correct(arr, k):
    return bisect_left(arr, k)
