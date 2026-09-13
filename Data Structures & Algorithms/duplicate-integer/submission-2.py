class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        now = set()
        for i in nums:
            if i in now:
                return True
            now.add(i)
        return False