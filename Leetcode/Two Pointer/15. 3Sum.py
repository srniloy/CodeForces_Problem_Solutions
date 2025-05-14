class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i, a in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                sumA = a + nums[l] + nums[r]
                if sumA == 0:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                elif sumA > 0:
                    r-=1
                else:
                    l+=1
        return res



