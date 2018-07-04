class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res = 0
        if len(height) <= 2:
            return res
        index_left = 0
        index_right = 1
        while index_right < len(height):
            if height[index_right] >= height[index_left]:
                index_left += 1
                index_right = index_left + 1
                continue
            tmp_index = index_right
            while tmp_index < len(height) and height[tmp_index] < height[index_left]:
                tmp_index += 1

            if tmp_index == len(height):
                tmp_index_1 = index_right
                tmp_index_2 = index_right + 1
                while tmp_index_1 < len(height) and tmp_index_2 < len(height) \
                        and height[tmp_index_1] >= height[tmp_index_2]:
                    tmp_index_1 += 1
                    tmp_index_2 += 1
                if tmp_index_2 == len(height):
                    return res

                heightmax = 0
                for j in range(index_left + 1, len(height)):
                    if height[j] > heightmax:
                        heightmax = height[j]
                        tmp_index = j
                if tmp_index != index_left + 1:
                    for j in range(index_left + 1, tmp_index):
                        res += height[tmp_index] - height[j]

            else:
                for j in range(index_left + 1, tmp_index):
                    res += height[index_left] - height[j]
            index_left = tmp_index
            index_right = index_left + 1
        return res

height = [2,8,5,5,6,1,7,2]
obj = Solution()
ans = obj.trap(height)
print(ans)