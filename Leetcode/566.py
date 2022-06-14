"""
566. Reshape the Matrix
"""
import itertools
from typing import List

import pytest
def matrixReshape(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    m, n = len(mat), len(mat[0])
    if m*n != r*c: return mat
    """
    Notice: the matrix initialization!!!
    """
    res = [[0 for i in range(c)] for j in range(r)]
    #res = [[0]*c]*r not good, very bad
    # res = [].append(range(r,c))WRONG
    mat_list = [j for i in range(m) for j in mat[i]]
    # print(res, mat_list)
    k = 0
    for i in range(r):
        for j in range(c):
            res[i][j] = mat_list[k]
            print(i, j, res, mat_list[k], k)
            k += 1
    return res


# very good answers
def matrixReshape1(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    flat = sum(mat, [])
    if len(flat) != r * c:
        return mat
    tuples = zip(*([iter(flat)] * c))
    return map(list, tuples)
    #return mat if len(sum(mat, [])) != r * c else map(list, zip(*([iter(sum(mat, []))]*c)))

def matrixReshape2(mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    if r * c != len(mat) * len(mat[0]):
        return mat
    it = itertools.chain(*mat)
    return [list(itertools.islice(it, c)) for _ in range(r)]

test_case = [
    ([[1,2],[3,4]], 1, 4, [[1,2,3,4]]),
    ([[1,2],[3,4]], 4, 1, [[1],[2],[3],[4]]),
    ([[1,2],[3,4]], 2, 1, [[1,2],[3,4]]),
    ([[1,2,3], [4,5,6]], 3, 2, [[1, 2], [3, 4], [5, 6]]),
    ([[1,2,3], [4,5,6]], 6, 1, [[1],[2],[3],[4],[5],[6]]),
]

@pytest.mark.parametrize("mat, r, c, expect", test_case)
def test_matrixReshape(mat: List[List[int]], r: int, c: int, expect: List[List[int]])->None:
    assert matrixReshape(mat, r, c) == expect