class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        listofutf8 = []
        for i in range(0, len(data)):
            tmpstring = bin(data[i])
            tmpstring = tmpstring[2:]
            tmpn = len(tmpstring)
            if tmpn > 8:
                tmpstring = tmpstring[tmpn-8 : ]
            if tmpn < 8:
                tmpstring2 = ''
                for j in range(0, 8-tmpn):
                    tmpstring2 = tmpstring2 + '0'
                tmpstring = tmpstring2 + tmpstring


            listofutf8.append(tmpstring)
        #print(listofutf8)
        index = 0
        while index<len(data):
            if listofutf8[index][0] == '0':
                index = index+1
                continue
            if listofutf8[index][:5] == '11110':
                if index + 3 >= len(data) or listofutf8[index+1][:2] != '10' or listofutf8[index+2][:2] != '10' or listofutf8[index+3][:2] != '10':
                    return False
                index = index + 4
                continue
            if listofutf8[index][:4] == '1110':
                if index + 2 >= len(data) or listofutf8[index+1][:2] != '10' or listofutf8[index+2][:2] != '10':
                    return False
                index = index + 3
                continue
            if listofutf8[index][:3] == '110':
                if index + 1 >= len(data) or listofutf8[index+1][:2] != '10':
                    return False
                index = index + 2
                continue

            return False

        return True






data = [235, 140, 4]
obj = Solution()
ans = obj.validUtf8(data)
print(ans)
