def productExceptSelf(self, nums):

    def cal(nums, i):
        pro = 1
        for j in range(len(nums)):
            if i != j:
                pro = pro * nums[j]

        return pro

    result = [1] * len(nums)

    for i in range(len(nums)):
        result[i] = cal(nums, i)

    return result


#another Way
#User function Template for python3


class Solution:

    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        result = [0] * n

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]

        for i in range(n - 2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]

        for i in range(n):
            result[i] = right[i] * left[i]

        return result
