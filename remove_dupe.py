class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return
        slow = fast = 0
        while fast <= len(nums) - 1:
            if nums[fast] != nums[slow]:
                nums[slow+1] = nums[fast]
                slow += 1
            fast += 1
        return slow + 1

nums = [1,2,3,3]




class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = list(dict.fromkeys(nums))
        return len(nums)

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(set(nums))
        return len(nums)