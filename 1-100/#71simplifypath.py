class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        index = 0
        current = ""
        path = path + "/"
        st = []
        for i in range(0, len(path)):
            if path[i] == '/':
                if current == "..":
                    if st:
                        st.pop()
                else:
                    if current != "." and len(current) > 0:
                        st.append(current)
                current = ""
            else:
                current += path[i]
        res = ""
        while st:
            res = "/" + st[-1] + res
            st.pop()
        if len(res) == 0:
            return "/"
        else:
            return res

path = '/.'
obj = Solution()
ans = obj.simplifyPath(path)
print(ans)