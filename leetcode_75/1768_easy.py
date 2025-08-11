# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

# Return the merged string.

# Example 1:

# Input: word1 = "abc", word2 = "pqr"
# Output: "apbqcr"
# Explanation: The merged string will be merged as so:
# word1:  a   b   c
# word2:    p   q   r
# merged: a p b q c r
# Example 2:

# Input: word1 = "ab", word2 = "pqrs"
# Output: "apbqrs"
# Explanation: Notice that as word2 is longer, "rs" is appended to the end.
# word1:  a   b 
# word2:    p   q   r   s
# merged: a p b q   r   s
# Example 3:

# Input: word1 = "abcd", word2 = "pq"
# Output: "apbqcd"
# Explanation: Notice that as word1 is longer, "cd" is appended to the end.
# word1:  a   b   c   d
# word2:    p   q 
# merged: a p b q c   d
 

# Constraints:

# 1 <= word1.length, word2.length <= 100
# word1 and word2 consist of lowercase English letters.

def mergeAlternately(word1: str, word2: str) -> str:
    word1_arr, word2_arr = list(word1), list(word2)
    sol = ""
    while len(word1_arr) != 0 and len(word2_arr) != 0:
        sol += (word1_arr[0])
        sol += (word2_arr[0])
        word1_arr.pop(0)
        word2_arr.pop(0)
    if len(word1_arr) == 0:
        rem = ''.join(word2_arr)
        sol += (rem)
    else:
        rem = ''.join(word1_arr)
        sol += (rem)
    return sol

print(mergeAlternately("abc", "pqr"))