class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        appears = []
        for num in nums:
            if num in appears:
                return True
            appears.append(num)
        return False
