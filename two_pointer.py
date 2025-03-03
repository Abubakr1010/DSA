class Solution:
    def removePalindromeSub(self, s: str) -> int:
        left = 0
        right = len(s) - 1

        while left < right:
            if left[s] != right[s]:
                return 2
            left += 1
            right -= 1

        return 1



