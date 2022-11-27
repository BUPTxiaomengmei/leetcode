class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        sum_list = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 ==0:
                sum_list.append('FizzBuzz')
            elif i % 3 == 0:
                sum_list.append('Fizz')
            elif i % 5 == 0:
                sum_list.append('Buzz')
            else:
                sum_list.append(str(i))
        return sum_list

solution = Solution()
print(solution.fizzBuzz(15))