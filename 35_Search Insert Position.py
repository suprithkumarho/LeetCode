"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
"""


class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r :
            mid = (l+r)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                    r = mid - 1
            elif nums[mid] < target:
                    l = mid + 1
            
        return l
    
nums = [1,3]
target = 2
sol = Solution()
print(sol.searchInsert(nums,target))