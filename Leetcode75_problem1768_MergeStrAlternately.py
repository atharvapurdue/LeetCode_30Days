# %%
# %%
'''
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.

 

Example 1:

Input: word1 = "abc", word2 = "pqr"
Output: "apbqcr"
Explanation: The merged string will be merged as so:
word1:  a   b   c
word2:    p   q   r
merged: a p b q c r
Example 2:

Input: word1 = "ab", word2 = "pqrs"
Output: "apbqrs"
Explanation: Notice that as word2 is longer, "rs" is appended to the end.
word1:  a   b 
word2:    p   q   r   s
merged: a p b q   r   s
Example 3:

Input: word1 = "abcd", word2 = "pq"
Output: "apbqcd"
Explanation: Notice that as word1 is longer, "cd" is appended to the end.
word1:  a   b   c   d
word2:    p   q 
merged: a p b q c   d
'''
# %%
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1,len2 = len(word1), len(word2)
        if len1 <= len2:
            min_length = len1
            flag=0
        else:
            min_length = len2
            flag =1
        alt_str = ""
        for i in range(0,min_length):
            alt_str=alt_str + word1[i]
            alt_str=alt_str + word2[i]
       
        if flag ==0:
            alt_str=alt_str + word2[i+1:]
        else:
            alt_str=alt_str + word1[i+1:]
        return alt_str
        
# %% 
