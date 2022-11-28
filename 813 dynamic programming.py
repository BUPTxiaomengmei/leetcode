# 给定数组nums和一个整数k。我们将给定的数组nums分成 最多k个相邻的非空子数组 。分数 由每个子数组内的平均值的总和构成。
#
# 注意我们必须使用 nums 数组中的每一个数进行分组，并且分数不一定需要是整数。
#
# 返回我们所能得到的最大 分数 是多少。答案误差在10-6内被视为是正确的。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode.cn/problems/largest-sum-of-averages
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# class Solution:
#     def largestSumOfAverages(self,nums,k):
#         n = len(nums)
#         psum = [0] * ()

class Solution:
    def largestSumOfAverages(self, nums, k):
        length = len(nums)
        dp = [[0.0] * (k + 1) for _ in range(length + 1)]
        prefix = [0.0] * (length + 1)
        presum = 0
        for i in range(1, length + 1):  # 构造 prefix 数组(列表)
            presum += nums[i - 1]
            prefix[i] = presum

        for i in range(1, length + 1):  # j = 1 的情况下对第一列进行初始化
            dp[i][1] = prefix[i] / i

        for j in range(2, k + 1):  # j > 1 的情况
            for i in range(j, length + 1):
                for x in range(j - 1, i):
                    dp[i][j] = max(dp[i][j], dp[x][j - 1] + (prefix[i] - prefix[x]) / (i - x))
        return dp[length][k]

solution = Solution()
print(solution.largestSumOfAverages([4,1,7,5,6,2,3],4))