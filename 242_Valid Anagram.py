"""
Valid Anagram
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
 

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.
"""

class Solution:
    def Anagram(self, s: str, t: str)  -> bool :
        '''
        Approach 1
        if len(s) != len(t):
            return False
        
        sres = {}

        for i in s:
            if i not in sres.keys():
                sres[i] = 1
            else:
                sres[i] += 1
        
        tres = {}

        for i in t:
            if i not in tres.keys():
                tres[i] = 1
            else:
                tres[i] += 1
        
        
        return sres == tres
        '''
        if len(s) != len(t):
            return False
        
        sSorted = sorted(list(s))
        tSorted = sorted(list(t))
        
        return sSorted ==tSorted

s = "jar"
t = "jam"
#s = "racecar"
#t = "carrace"
sol = Solution()
print(sol.Anagram(s,t))