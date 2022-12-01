class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        distance = None
        index = None
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                # 有效
                if distance == None or abs(points[i][0] - x) + abs(points[i][1] - y) < distance:
                    distance = abs(points[i][0] - x) + abs(points[i][1] - y)
                    index = i
        if index == None:
            return -1
        return index

solution = Solution()
print(solution.nearestValidPoint(3,
4,
[[1,2],[3,1],[2,4],[2,3],[4,4]]))