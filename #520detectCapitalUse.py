class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if len(word) == 1:
            return True

        if ord(word[0]) < ord('A') or ord(word[0]) > ord('Z'):  # First small, all must be small
            for i in range(0, len(word)):
                if ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
                    return False
            return True
        else:  # First Large
            allLarge = True  # all large
            for i in range(0, len(word)):
                if ord(word[i]) < ord('A') or ord(word[i]) > ord('Z'):
                    allLarge = False
                    break
            allsmall = True  # last are small
            for i in range(1, len(word)):
                if ord(word[i]) >= ord('A') and ord(word[i]) <= ord('Z'):
                    allsmall = False
                    break
            if allsmall or allLarge:
                return True

            return False