class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        n = len(secret)
        a = 0
        b = 0
        i = 0

        while i < n:
            if secret[i] == guess[i]:
                a = a + 1
                secret = secret[0: i] + secret[i + 1: n]
                guess = guess[0: i] + guess[i + 1: n]
                n = n - 1
            else:
                i = i + 1

        secret2 = []
        guess2 = []
        for i in range(0, n):
            secret2.append(secret[i])
            guess2.append(guess[i])

        secret2.sort()
        guess2.sort()
        i = 0
        j = 0
        while (i < n) and (j < n):
            if secret2[i] == guess2[j]:
                b = b + 1
                i = i + 1
                j = j + 1
            else:
                if secret2[i] > guess2[j]:
                    j = j + 1
                else:
                    i = i + 1

        ans = str(a) + "A" + str(b) + "B"

        return ans