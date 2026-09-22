class Solution(object):
    def isPalindrome(self, x):
        value=str(x)
        data=value[::-1]
        if value==data:
            return True
        else:
            return False
