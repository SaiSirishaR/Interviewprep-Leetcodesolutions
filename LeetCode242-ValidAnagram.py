class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

### Condition1: lengths of both the strings are same?
### Condition2: letters in string 's' are also present in string 't'?
### Condition3: Number of occurances of each letter in both the strings is the same?
        return sorted(s) == sorted(t)
