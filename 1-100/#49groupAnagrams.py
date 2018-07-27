class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dict = {}
        for i in strs:
            tmp = "".join(sorted(i))
            #print(tmp)
            if not dict.has_key(tmp):
                #dict[tmp] = i
                #dict[tmp] = []
                dict[tmp] = [i]
            else:
                #dict[tmp] += '#' + i
                dict[tmp].append(i)
        #print(dict)
        res = []
        for i in dict:
            res.append(dict[i])
        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
obj = Solution()
ans = obj.groupAnagrams(strs)
print(ans)