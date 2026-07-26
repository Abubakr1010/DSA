class Solution:
    def isPalindrome(self, s: str) -> bool:
        # --- RULES ---
        # converting all alpha-numeric to lowercase
        # removing non-alpha numeric character

        # --- EDGE CASES ---
        # return true if palindrome else false
        # empty string return true

        # --- SOLUTION ---
        if s is None:
            return True

        new_s = "".join(char.lower() for char in s if char.isalnum())

        if new_s is None:
            return True

        left, right = 0, len(new_s) - 1

        while left < right:
            if new_s[left] == new_s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True

         






        