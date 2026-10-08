class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        total = n * (n+1)//2
        sum1 = 0
        for num in nums:
            sum1 += num
        return total-sum1
        