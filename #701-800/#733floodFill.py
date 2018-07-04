class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """

        def myfloodfill(image, sr, sc, newColor, index):

            if (0 <= sr < len(image)) and (0 <= sc < len(image[0])) and (image[sr][sc] == index):
                image[sr][sc] = newColor
                myfloodfill(image, sr + 1, sc, newColor, index)
                myfloodfill(image, sr - 1, sc, newColor, index)
                myfloodfill(image, sr, sc + 1, newColor, index)
                myfloodfill(image, sr, sc - 1, newColor, index)

        index = image[sr][sc]
        myfloodfill(image, sr, sc, -1, index)
        for i in range(0, len(image)):
            for j in range(0, len(image[0])):
                if (image[i][j] == -1):
                    image[i][j] = newColor

        return image