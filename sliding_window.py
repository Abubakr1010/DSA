#All leetcode solutions related sliding window


# 1652. Defuse the Bomb

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        if k == 0:
            return [0] * n  # If k == 0, replace all numbers with 0

        decrypted = [0] * n  # Initialize the result array

        for i in range(n):
            total = 0
            if k > 0:  # Sum next k elements
                for j in range(1, k + 1):
                    total += code[(i + j) % n]  # Circular indexing
            else:  # Sum previous |k| elements
                for j in range(1, abs(k) + 1):
                    total += code[(i - j) % n]  # Circular indexing
            decrypted[i] = total  # Store the sum

        return decrypted

