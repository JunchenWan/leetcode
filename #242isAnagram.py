class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_dict = {}
        t_dict = {}
        for i in s:
            if s_dict.has_key(i):
                s_dict[i] += 1
            else:
                s_dict[i] = 1
        for i in t:
            if t_dict.has_key(i):
                t_dict[i] += 1
            else:
                t_dict[i] = 1
        for k in s_dict:
            if not t_dict.has_key(k) or s_dict[k] != t_dict[k]:
                return False
        for k in t_dict:
            if not s_dict.has_key(k) or s_dict[k] != t_dict[k]:
                return False
        return True