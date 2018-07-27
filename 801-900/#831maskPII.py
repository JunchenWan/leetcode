class Solution(object):
    def maskPII(self, S):
        """
        :type S: str
        :rtype: str
        """
        if '@' in S:
            S = S.lower()
            tmp1 = S.index('@')
            tmpS1 = S[:tmp1]
            tmpS2 = S[tmp1:]
            res = tmpS1[0]+'*****'+tmpS1[-1]+tmpS2
        else:
            index = len(S)-1
            count = 0
            S3 = ''
            while count<4:
               if ord(S[index])<=ord('9') and ord(S[index])>=ord('0'):
                   S3 = S[index] + S3
                   count = count+1
                   index -= 1
               else:
                   index -= 1
            S2 = '***-***-'
            count = 0
            for i in range(0, len(S)):
                if ord(S[i]) <= ord('9') and ord(S[i]) >= ord('0'):
                    count += 1
            if count == 13:
                res = '+***-'+S2+S3
            if count == 12:
                res = '+**-'+S2+S3
            if count == 11:
                res = '+*-'+S2+S3
            if count==10:
                res = S2+S3

        return res

S = "86-(10)12345678"
obj = Solution()
ans = obj.maskPII(S)
print(ans)