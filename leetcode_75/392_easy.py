# Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
#
# A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).
#
#
#
# Example 1:
#
# Input: s = "abc", t = "ahbgdc"
# Output: true
# Example 2:
#
# Input: s = "axc", t = "ahbgdc"
# Output: false
#
#
# Constraints:
#
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.
#
#
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

def isSubsequence(s: str, t: str) -> bool:
    t_index = 0
    s_index = 0
    if len(list(s)) == 0:
        return True
    if len(list(t)) == 0:
        return False

    flag = False
    while not flag:
        print(list(s)[s_index], list(t)[t_index])
        if list(s)[s_index] == list(t)[t_index]:
            if s_index == len(s) - 1: # last element of substring
                flag = True
            elif t_index == len(t) - 1: # last element of actual string & doesn't match with substring
                return False
            else: # continue checking
                t_index += 1
                s_index += 1
        else: # they aren't equal
            if t_index == len(t) - 1: #t_index was last element, checked all of substring
                return False
            else:
                t_index += 1 # increment by 1
    return flag

def isSubsequence2(s: str, t: str) -> bool:
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j += 1
    return i == len(s)


print(isSubsequence2("abc", "ahbgdc"))