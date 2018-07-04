"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """

        for i in range(0, len(employees)):
            if employees[i].id == id:
                ans = 0
                ans = ans + employees[i].importance
                for j in range(0, len(employees[i].subordinates)):
                    ans = ans + self.getImportance(employees, employees[i].subordinates[j])
                break
        return ans