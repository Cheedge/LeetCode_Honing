from collections import Counter
def solve(s1: str, s2: str)->bool:
    cnt1 = Counter(s1)
    cnt2 = Counter(s2)
    if cnt1 == cnt2:
        return True
    else:
        return False


#  (), ()    -> true
#     #       -> false
#      keen - care 

print(solve("keen", "care"))