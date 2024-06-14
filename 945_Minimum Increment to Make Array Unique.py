'''
You are given an integer array nums. 
In one move, you can pick an index i where 0 <= i < nums.length and increment nums[i] by 1.

Return the minimum number of moves to make every value in nums unique.

The test cases are generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: nums = [1,2,2]
Output: 1
Explanation: After 1 move, the array could be [1, 2, 3].
Example 2:

Input: nums = [3,2,1,2,1,7]
Output: 6
Explanation: After 6 moves, the array could be [3, 4, 1, 2, 5, 7].
It can be shown with 5 or less moves that it is impossible for the array to have all unique values.
=========================================================================
Approach:
- Sort the list. Check if the current element is less than expected element, if so increment the current element to expected element and add the number of moves.
- If the current element is greater than or equal to expected element, just assign the current element to expected element and increment expected element by 1 as the next expected should be unique.
=========================================================================
'''

class Solution:
    def minIncrementForUnique(self, nums: list[int]) -> int:
        nums.sort()

        moves = 0
        next_expected = nums[0]

        for curr_item in nums:
            if curr_item < next_expected:
                moves += next_expected - curr_item
            else:
                next_expected = curr_item
            next_expected += 1
        
        return moves

    
nums = [3,2,1,2,1,7]  
sol = Solution()
print(sol.minIncrementForUnique(nums))