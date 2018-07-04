class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        ni = len(M)
        nj = len(M[0])
        ans = [[0 for j in range(0,nj)] for i in range(0, ni)]
        for i in range(0, ni):
            for j in range(0, nj):
                tmpsum = M[i][j]
                tmpcount = 1
                if i-1>=0:
                    tmpsum += M[i-1][j]
                    tmpcount += 1
                if (i-1>=0)and(j+1<nj):
                    tmpsum += M[i-1][j+1]
                    tmpcount += 1
                if j+1<nj:
                    tmpsum += M[i][j+1]
                    tmpcount += 1
                if (i+1<ni)and(j+1<nj):
                    tmpsum += M[i+1][j+1]
                    tmpcount += 1
                if i+1<ni:
                    tmpsum += M[i+1][j]
                    tmpcount += 1
                if (i+1<ni)and(j-1>=0):
                    tmpsum += M[i+1][j-1]
                    tmpcount += 1
                if j-1>=0:
                    tmpsum += M[i][j-1]
                    tmpcount += 1
                if (j-1>=0)and(i-1>=0):
                    tmpsum += M[i-1][j-1]
                    tmpcount += 1
                ans[i][j] = tmpsum//tmpcount
        return ans

M = [[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]]
obj = Solution()
ans = obj.imageSmoother(M)
print(ans)