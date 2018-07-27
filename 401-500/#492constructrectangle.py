class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        import numpy as np
        length = int(np.sqrt(area))

        while length <= area:
            width = area / length
            if length * width == area:
                return [max(length, width), min(length, width)]
            length = length + 1