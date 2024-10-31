"""
966. Vowel Spellchecker

Medium

Given a wordlist, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:

Capitalization: If the query matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the case in the wordlist.
Example: wordlist = ["yellow"], query = "YellOw": correct = "yellow"
Example: wordlist = ["Yellow"], query = "yellow": correct = "Yellow"
Example: wordlist = ["yellow"], query = "yellow": correct = "yellow"
Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually, it matches a word in the wordlist (case-insensitive), then the query word is returned with the same case as the match in the wordlist.
Example: wordlist = ["YellOw"], query = "yollow": correct = "YellOw"
Example: wordlist = ["YellOw"], query = "yeellow": correct = "" (no match)
Example: wordlist = ["YellOw"], query = "yllw": correct = "" (no match)
In addition, the spell checker operates under the following precedence rules:

- When the query exactly matches a word in the wordlist (case-sensitive), you should return the same word back.
- When the query matches a word up to capitlization, you should return the first such match in the wordlist.
- When the query matches a word up to vowel errors, you should return the first such match in the wordlist.
- If the query has no matches in the wordlist, you should return the empty string.

Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].

 

Example 1:

Input: wordlist = ["KiTe","kite","hare","Hare"], queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
Output: ["kite","KiTe","KiTe","Hare","hare","","","KiTe","","KiTe"]
Example 2:

Input: wordlist = ["yellow"], queries = ["YellOw"]
Output: ["yellow"]
 

Constraints:

1 <= wordlist.length, queries.length <= 5000
1 <= wordlist[i].length, queries[i].length <= 7
wordlist[i] and queries[i] consist only of only English letters.

"""

class Solution:
    def spellchecker(self, wordlist: list[str], queries: list[str]) -> list[str]:
        wordset = set(wordlist)
        wordUpper = {}
        wordMask = {}

        for word in wordlist:
            # creating template of uppercase word, which will be used to match with uppercase query word
            if word.upper() not in wordUpper:
                wordUpper[word.upper()] = word
            
            # creating template of mask word, which will be used to match with masked query word
            mask = "".join('*' if w.lower() in "aeiou" else w for w in word.lower())
            if mask not in wordMask:
                wordMask[mask] = word
        
        res = []

        for q in queries:
            curr = ""
            #checking the if its a exact match
            if q in wordset:
                curr = q
            #checking the if uppercase word is already present in wordUpper
            elif q.upper() in wordUpper:
                curr = wordUpper[q.upper()]
            #checking the if masked word is already present in wordmask
            else:
                qmask = "".join("*" if qw.lower() in "aeiou" else qw for qw in q.lower())
                if qmask in wordMask:
                    curr = wordMask[qmask]
            res.append(curr)
        #print(res)
        return res
            
                
        print(wordset)
        print(wordUpper)
        print(wordMask)

if __name__ == "__main__":
    wordlist = ["KiTe","kite","hare","Hare"]
    queries = ["kite","Kite","KiTe","Hare","HARE","Hear","hear","keti","keet","keto"]
    sol = Solution()
    print(sol.spellchecker(wordlist,queries))

