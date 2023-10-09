class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        store = {}
        for i in nums:
            store [i] = True
        missing_num=-1
        for i in range(0,len(nums) + 1):
            if i not in store:
                missing_num=i
                break
        return missing_num

