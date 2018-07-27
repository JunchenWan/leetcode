# """
# This is Master's API interface.
# You should not implement it, or speculate about its implementation
# """
# class Master(object):
#    def guess(self, word):
#        """
#        :type word: str
#        :rtype int
#        """

class Solution(object):
    def findSecretWord(self, wordlist, master):
        """
        :type wordlist: List[Str]
        :type master: Master
        :rtype: None
        """
        import random

        for i in range(0, 10):
            random.shuffle(wordlist) #without this line, the code will not be accepted.
            guess = wordlist[0]
            nums = master.guess(guess)
            if nums == 6: break
            tmplist = []
            for j in range(0, len(wordlist)):
                equal = 0
                for k in range(0, 6):
                    if guess[k] == wordlist[j][k]:
                        equal += 1
                if equal == nums:
                    tmplist.append(wordlist[j])
            wordlist = [] + tmplist