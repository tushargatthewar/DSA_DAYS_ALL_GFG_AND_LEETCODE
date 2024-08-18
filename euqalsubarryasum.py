class Solution:

    def canSplit(self, arr):
        left = 0
        right = len(arr) - 1
        left_sum = arr[left]
        right_sum = arr[right]

        # total= sum(arr)

        # if total%2 !=0:
        #     return False

        # half=total//2
        # sum1=0

        # for i in arr:
        #     sum1+=i
        #     if sum1==half:
        #         return True

        # return False

        while left < right:
            if left_sum < right_sum:
                left += 1
                left_sum += arr[left]
            elif right_sum < left_sum:
                right -= 1
                right_sum += arr[right]
            else:

                if left + 1 == right:
                    return True
                left += 1
                left_sum += arr[left]
                right -= 1
                right_sum += arr[right]

        return False
