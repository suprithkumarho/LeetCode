'''
 Find the Duplicate Number
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.

 

Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
Example 3:

Input: nums = [3,3,3,3,3]
Output: 3
'''

class Solution():
    def duplicatInteger(self, nums: list[int]) -> int:
        '''
        Approach 1 : if requirement is only to return true or false

        numslen = len(nums)
        numsSetlen = len(set(nums))
        if numslen == numsSetlen:
            return True
        else:
            return False
        '''
        res = {}

        for i in nums:
            if i in res.keys():
                return i
            else:
                res[i] = 1

nums = [1, 2, 3, 3]
#nums = [1, 2, 3, 4]
sol = Solution()
print(sol.duplicatInteger(nums))