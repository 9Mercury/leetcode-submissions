class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        i = 0
        res = []
        while i < len(nums):
            mul = 1  # Initialize mul for each iteration of the outer loop
            for j in range(0,len(nums)):
                if j != i:
                    mul *= nums[j]
            res.append(mul)
            i += 1 # Increment i to avoid infinite loop
        return res
        