class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {p:j for j,p in enumerate(nums)}
        for i,v in enumerate(nums):
            x = target - v
            if x in hash and hash[x]!=i:
                return [i,hash[x]]