class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morsecode = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.",
                     "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        lengthofwords = len(words)
        count = 0
        morse = []
        for i in range(0, lengthofwords):
            tmp = ''
            for j in range(0, len(words[i])):
                tmp = tmp + morsecode[ord(words[i][j]) - 97]

            judge = True
            for j in range(0, count):
                if morse[j] == tmp:
                    judge = False
                    break
            if judge:
                morse.append(tmp)
                count += 1

        return count

    return count