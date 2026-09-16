class Solution(object):
    def findDisappearedNumbers(self,nums):
        for n in nums:
            index = abs(n) - 1
            if nums[index] > 0:
                nums[index] = -nums[index]
            
        result = []
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)
            
        return result