'''
Relative Sort Array
Given two arrays arr1 and arr2, the elements of arr2 are distinct, 
and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
Elements that do not appear in arr2 should be placed at the end of arr1 in ascending order.

 
Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
Example 2:

Input: arr1 = [28,6,22,8,44,17], arr2 = [22,28,8,6]
Output: [22,28,8,6,17,44]
 

Constraints:

1 <= arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
All the elements of arr2 are distinct.
Each arr2[i] is in arr1.
=========================================================================
Approach:

1. Count occurrences of each element in 'arr1' using a dictionary.
2. For each element in 'arr2', add it to the result list according to its count in 'arr1' and remove it from the dictionary.
3. Add the remaining elements not in 'arr2' to the result list in sorted order.

Time Complexity:
- Counting elements in 'arr1': (O(n))
- Adding elements from 'arr2' to result: (O(m))
- Sorting remaining elements: (O(k log k))
Overall: (O(n + m + k log k)), where (n) is the length of 'arr1', (m) is the length of 'arr2', and (k) is the number of remaining elements in 'arr1'.

Space Complexity:
- Space for the dictionary and the result list: (O(n))
=========================================================================
'''

class Solution:
    def relativeSortArray(self, arr1: list[int], arr2: list[int]) -> list[int]:

        res = []
        eleCount = {}
        #adding the each element and its count to the dictonary
        for i in arr1:
            if i not in eleCount.keys():
                eleCount[i] = 1
            else:
                eleCount[i] += 1

        #adding the element matched with arr2 to the res by replicating its occurance count
        for ele in arr2:
            if ele in eleCount.keys():
                res.extend([ele] * eleCount[ele])
                eleCount.pop(ele)

        # sorting the remaing elements in the dict and adding it to the res
        remEle = sorted(eleCount.keys())
        for rele in remEle:
            res.extend([rele] * eleCount[rele])
        return res

arr1 = [2,3,1,3,2,4,6,7,9,2,19]
arr2 = [2,1,4,3,9,6]
sol = Solution()
print(sol.relativeSortArray(arr1, arr2))


