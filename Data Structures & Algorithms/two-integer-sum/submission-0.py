class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = defaultdict(int)
        for i in range(len(nums)):
            value=target-nums[i]
            if value in my_dict:
                return sorted([i,my_dict[value]])
            my_dict[nums[i]]=i
        
