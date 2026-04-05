class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        noDupe = set(nums)
        return len(noDupe) < len(nums)