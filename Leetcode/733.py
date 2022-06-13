"""
733. Flood Fill

An image is represented by an m x n integer grid image where 
image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You 
should perform a flood fill on the image starting from the 
pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus 
any pixels connected 4-directionally to the starting pixel 
of the same color as the starting pixel, plus any pixels 
connected 4-directionally to those pixels (also with the 
same color), and so on. Replace the color of all of the 
aforementioned pixels with newColor.

Return the modified image after performing the flood fill.


Example 1:


Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), 
all pixels connected by a path of the same color as the starting pixel 
(i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally 
connected to the starting pixel.

Example 2:

Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
 

Constraints:

m == image.length
n == image[i].length
1 <= m, n <= 50
0 <= image[i][j], newColor < 216
0 <= sr < m
0 <= sc < n
"""
from cgi import test
import pytest


def floodFill(image, sr, sc, newColor):
    def DFS(image, i, j, nc, c):
        # print(image)
        m, n = len(image), len(image[0])
        if i+1<m and image[i+1][j] == c:
            image[i+1][j] = nc
            DFS(image, i+1, j, nc, c)
        if i-1>=0 and image[i-1][j] == c:
            # print(image, c, nc, i, j)
            image[i-1][j] = nc
            DFS(image, i-1, j, nc, c)
        if j+1<n and image[i][j+1] == c:
            # print(image, c, nc, i, j)
            image[i][j+1] = nc
            DFS(image, i, j+1, nc, c)
        if j-1>=0 and image[i][j-1] == c:
            image[i][j-1] = nc
            DFS(image, i, j-1, nc, c)
    """
    here set painting color to -1, because newColor>0, 
    then after paint reset all painted block to newColor
    """
    DFS(image, sr, sc, -1, image[sr][sc])
    image[sr][sc] = -1
    for i in range(len(image)):
        for j in range(len(image[0])):
            if image[i][j]==-1:
                image[i][j] = newColor
    return image

test_case = [
    ([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2,[[2,2,2],[2,2,0],[2,0,1]]),
    ([[0,0,0],[0,1,0]], 1, 1, 3, [[0,0,0],[0,3,0]]),
    ([[0,0,0],[0,1,1]], 1, 1, 1, [[0,0,0],[0,1,1]]),
]

@pytest.mark.parametrize("image, sr, sc, newColor, expect", test_case)
def test_floodFill(image, sr, sc, newColor, expect):
    assert floodFill(image, sr, sc, newColor) == expect