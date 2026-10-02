class Solution(object):
    def majorityElement(self, nums):
        count = candidate = 0
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else:
                count -= 1
        return candidate
