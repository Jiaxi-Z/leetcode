from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        for num in self.nums:
            num_index = self.nums.index(num)
            result = self.target - num
            if result in self.nums[num_index+1:]:
                result_index = self.nums[num_index +
                                         1:].index(result) + num_index + 1
                return [num_index, result_index]


nums = [2, 7, 11, 15]
target = 9

a = Solution()
print(a.twoSum(nums, target))
