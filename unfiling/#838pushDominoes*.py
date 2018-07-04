class Solution(object):
    def pushDominoes(self, dominoes):
        """
        :type dominoes: str
        :rtype: str
        """

        if len(dominoes) <= 1:
            return dominoes

        res = ""
        index = 0
        while index < len(dominoes):
            if dominoes[index] == 'L' or dominoes[index] == 'R':
                res = res + dominoes[index]
                index += 1
            else:
                count_left = index
                count_right = index
                while count_left >= 0 and dominoes[count_left] == '.':
                    count_left -= 1
                while count_right < len(dominoes) and dominoes[count_right] == '.':
                    count_right += 1

                if count_left < 0 and count_right >= len(dominoes):
                    return dominoes

                if count_left < 0 and count_right < len(dominoes):
                    if dominoes[count_right] == 'L':
                        res = res + 'L'
                        index += 1
                        continue
                    else:
                        res = res + '.'
                        index += 1
                        continue

                if count_right >= len(dominoes) and count_left >= 0:
                    if dominoes[count_left] == 'R':
                        res = res + 'R'
                        index += 1
                        continue
                    else:
                        res = res + '.'
                        index += 1
                        continue

                if dominoes[count_left] == 'L' and dominoes[count_right] == 'L':
                    res = res + 'L'
                    index += 1
                    continue
                if dominoes[count_left] == 'R' and dominoes[count_right] == 'L':
                    if index - count_left == count_right - index:
                        res = res + '.'
                        index += 1
                        continue
                    if index - count_left < count_right - index:
                        res = res + 'R'
                        index += 1
                        continue
                    if index - count_left > count_right - index:
                        res = res + 'L'
                        index += 1
                        continue

                if dominoes[count_left] == 'R' and dominoes[count_right] == 'R':
                    res = res + 'R'
                    index += 1
                    continue
                if dominoes[count_left] == 'L' and dominoes[count_right] == 'R':
                    res = res + '.'
                    index += 1
                    continue

        return res

dominoes = ".L.R."
obj = Solution()
ans = obj.pushDominoes(dominoes)
print(ans)