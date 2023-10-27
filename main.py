# given array with n numbers in range [0, n]
# return the missing number
def missingNumber(self, nums: List[int]) -> int:
    result = len(nums)

    for i in range(len(nums)):
        result += i - nums[i]

    return result
