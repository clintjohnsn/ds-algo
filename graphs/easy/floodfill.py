"""
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and color.
perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel,
 plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel

  image =   [[1,1,1],
            [1,1,0],
            [1,0,1]], sr = 1, sc = 1, color = 2

Output: [[2,2,2],
        [2,2,0],
        [2,0,1]]
"""


class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int, oldcolor:int=None) -> list[list[int]]:
        if 0 <= sr < len(image) and 0 <= sc < len(image[0]):
            if oldcolor is None:
                oldcolor = image[sr][sc]
            if image[sr][sc] != color and image[sr][sc] == oldcolor:
                image[sr][sc] = color
                self.floodFill(image,sr+1,sc,color,oldcolor)
                self.floodFill(image,sr-1,sc,color,oldcolor)
                self.floodFill(image,sr,sc+1,color,oldcolor)
                self.floodFill(image,sr,sc-1,color,oldcolor)
        return image


image = [[1,1,1],[1,1,0],[1,0,1]]
print(Solution().floodFill(image,1,1,2))

image = [[0,0,0],[0,0,1]]
print(Solution().floodFill(image,0,0,2))
