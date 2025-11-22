feat: add solution for Two Sum (#1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        original_nums = nums[:]
        for num1 in nums:
            num1_index = nums.index(num1)
            if len(nums) > 1:
                popped_nums = nums[num1_index + 1 :]
            for num2 in popped_nums:
                if num1 + num2 == target:
                    ret_num1_index = original_nums.index(num1)
                    ret_num2_index = original_nums.index(num2)
                    ret = [ret_num1_index, ret_num2_index]
                    if num1 == num2:
                        ret = [i for i, num in enumerate(original_nums) if num == num1]
                    return ret
            if len(nums) > 1:
                num1_index = nums.index(num1)
                nums = nums[num1_index + 1 :]
