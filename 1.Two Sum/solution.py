class Solution(object):
    def twoSum(self, nums, target):
        result = []
        value_to_index_map = {}

        for i in range(0, len(nums)):

            if((target-nums[i]) in value_to_index_map):
                return[value_to_index_map[(target-nums[i])], i]
            value_to_index_map[nums[i]] = i


a = Solution()
print((a.twoSum([-3, 4, 3, 90], 0)))
