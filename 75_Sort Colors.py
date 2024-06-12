'''
Sort Colors
Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

You must solve this problem without using the library's sort function.

Example 1:

Input: nums = [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Example 2:

Input: nums = [2,0,1]
Output: [0,1,2]
 
Constraints:
n == nums.length
1 <= n <= 300
nums[i] is either 0, 1, or 2.

Follow up: Could you come up with a one-pass algorithm using only constant extra space?

=========================================================================
Approach:
- If nums[curr] is 0, swap it with nums[red], increment both curr and red.
- If nums[curr] is 2, swap it with nums[blue] and decrement blue (do not increment curr because the element swapped from blue needs to be checked).
- If nums[curr] is 1, just move curr forward.
=========================================================================

'''

class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        red , curr = 0,0
        blue = len(nums)-1

        while curr <= blue:

            print(f"red -->{red}\ncurr -->{curr}\nblue -->{blue}")
            print(nums)
            
            if nums[curr] == 0:
                temp = nums[curr]
                nums[curr] = nums[red]
                nums[red] = temp
                curr += 1
                red += 1

            elif nums[curr] == 2:
                temp = nums[curr]
                nums[curr] = nums[blue]
                nums[blue] = temp
                blue -= 1

            else:
                curr += 1
            

nums = [2,0,2,1,1,0]
sol = Solution()
sol.sortColors(nums)