class Solution(object):
    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        dict = {}
        for i in range(0, len(cpdomains)):
            tmpstr = cpdomains[i].split(' ')
            number = int(tmpstr[0])
            subdomain = tmpstr[1].split('.')[::-1]
            for j in range(0, len(subdomain)):
                if j == 0:
                    tmpName = subdomain[j]
                else:
                    tmpName = subdomain[j] + '.' + tmpName
                if tmpName in dict.keys():
                    dict[tmpName] += number
                else:
                    dict[tmpName] = number

        res = []
        for key in dict:
            tmpStr = str(dict[key]) + ' ' + key
            res.append(tmpStr)
        return res

cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
obj = Solution()
ans = obj.subdomainVisits(cpdomains)
print(ans)