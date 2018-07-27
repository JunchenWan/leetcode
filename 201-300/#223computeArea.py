class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """

        area = (C - A) * (D - B) + (G - E) * (H - F)
        # 判断两矩形左边的关系, 取靠右的边：
        if A < E:
            A = E
        else:
            E = A
        # 如果不重叠：
        if A >= C or E >= G:
            return area
        # 判断两矩形右边的关系，取靠左的边：
        if G > C:
            G = C
        else:
            C = G
        # 如果不重叠：
        if A >= C or E >= G:
            return area
        # 判断两矩形下边的关系，取靠上的边：
        if B < F:
            B = F
        else:
            F = B
        # 如果不重叠：
        if B >= D or F >= H:
            return area
        # 判断两矩形上边的关系，取靠下的边：
        if H < D:
            D = H
        else:
            H = D
        # 如果不重叠：
        if B >= D or F >= H:
            return area
        return area - (C - A) * (D - B)