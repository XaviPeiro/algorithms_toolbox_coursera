'''
Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that every character in t (including duplicates) is included in the window. If there is no such substring, return the empty string "".

The testcases will be generated such that the answer is unique.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"
Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
Example 2:

Input: s = "a", t = "a"
Output: "a"
Explanation: The entire string s is the minimum window.
Example 3:

Input: s = "a", t = "aa"
Output: ""
Explanation: Both 'a's from t must be included in the window.
Since the largest window of s only has one 'a', return empty string.

Constraints:

m == s.length
n == t.length
1 <= m, n <= 105
s and t consist of uppercase and lowercase English letters.

Follow up: Could you find an algorithm that runs in O(m + n) time?
'''

from collections import Counter

class Solution:
    def __call__(self, s: str, t: str) -> str:
        counter = Counter(t)
        required_char_countdown = len(t) 

        if required_char_countdown == 0:
            return ""
            
        il = 0

        res: None|str = None

        for i_char in range(len(s)):

            if s[i_char] in counter:
                counter[s[i_char]] -= 1

                if counter[s[i_char]] >= 0:
                    required_char_countdown -= 1


                if required_char_countdown == 0:
                    while il<i_char:
                        char = s[il]

                        if char in counter:
                            if counter[char] < 0:
                                counter[char] += 1
                            elif counter[char] == 0:
                                break
                            elif counter[char] > 0:
                                raise Exception("Impossible situation: This should never happen")

                        il += 1

                    # one solution here
                    if res is not None:
                        res = s[il:i_char+1] if len(res) > (i_char-il+1) else res
                    else:
                        res = s[il:i_char+1]
                        
                    if len(res) == 1:
                        return res

                    # if counter[]
                    counter[char] += 1 # This should never crash
                    required_char_countdown +=1
                    il += 1
        
        return res if res is not None else ""
        

s = Solution() 
assert s("ADOBECODEBANC", "ABC") == "BANC", s("ADOBECODEBANC", "ABC") if s("ADOBECODEBANC", "ABC") else "EMPTY"
