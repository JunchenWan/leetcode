class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        a = expression.split('/')
        parameters = []
        parameters.append(a[0])
        for i in range(1,len(a)):
            if (len(a[i].split('+'))==1)and(len(a[i].split('-'))==1):
                parameters.append(a[i])
            else:
                if (len(a[i].split('+'))==1):
                    temp = a[i].split('-')
                    parameters.append(temp[0])
                    parameters.append("-"+temp[1])
                else:
                    temp = a[i].split('+')
                    parameters.append(temp[0])
                    parameters.append(temp[1])

        for i in range(0,len(parameters)):
            parameters[i] = int(parameters[i])

        denomination = 1
        for i in range(0,len(parameters)):
            if (i%2 ==1):
                denomination = denomination * parameters[i]
        numerator = 0
        for i in range(0,len(parameters)):
            if (i%2 ==0):
                numerator = numerator + parameters[i]*denomination/parameters[i+1]

        if numerator==0:
            return "0/1"
        def gcm(a,b):
            if a>=b:
                if a % b == 0:
                    return b
                else:
                    return gcm(b, a-b)
            else:
                return gcm(b,a)

        if numerator>0:
            ans1 = numerator / gcm(denomination,numerator)
            ans2 = denomination / gcm(denomination,numerator)
        else:
            ans1 = numerator / gcm(denomination,-1*numerator)
            ans2 = denomination / gcm(denomination,-1*numerator)

        ans = "%d/%d" % (ans1,ans2)
        return ans