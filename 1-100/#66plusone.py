class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        if digits == [0]:
            return [1]
        digits = digits[::-1]
        digits[0] += 1
        index = 0
        while index < len(digits) and digits[index] >= 10:
            digits[index] = digits[index] % 10
            if index + 1 < len(digits):
                digits[index + 1] += 1
                index += 1
            else:
                digits.append(1)
                break
        digits = digits[::-1]
        return digits