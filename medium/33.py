class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while (l <= r):
            mid = (l + r) // 2

            if target == nums[mid]:
                return mid

            # 左側がソートされている場合
            if nums[l] <= target < nums[mid]:
                r = mid - 1
                continue
            else:
                l = mid + 1
                continue

            # 右側がソートされている場合
            if nums[mid] < target <= nums[r]:
                l = mid + 1
                continue
            else:
                r = mid - 1
                continue

        return -1
