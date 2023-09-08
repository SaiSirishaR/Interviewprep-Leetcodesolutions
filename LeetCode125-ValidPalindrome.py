class Solution:
    def isPalindrome(self, s: str) -> bool:

   # lower case = x.lower()
   # x.isalnum()
      p = []

      for i in range(0,len(s)):
       if s[i].isalnum():
          p.append(s[i].lower())
      return p == p[::-1]
