#All leetcode solutions related sliding window


# # 1652. Defuse the Bomb

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
#         if k == 0:
#             return [0] * n  # If k == 0, replace all numbers with 0

#         decrypted = [0] * n  # Initialize the result array

#         for i in range(n):
#             total = 0
#             if k > 0:  # Sum next k elements
#                 for j in range(1, k + 1):
#                     total += code[(i + j) % n]  # Circular indexing
#             else:  # Sum previous |k| elements
#                 for j in range(1, abs(k) + 1):
#                     total += code[(i - j) % n]  # Circular indexing
#             decrypted[i] = total  # Store the sum

#         return decrypted


# Testing and learning basic slidng window cocept

def max_sum_sub_array(arr, k):
    max_sum = float('inf')
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(len(arr) - k):
        window_sum = window_sum - arr[i] + arr[i + k]
        max_sum = max(max_sum, window_sum)

    return max_sum

arr = [2,1,5,1,3,2]
k = 3

print (max_sum_sub_array(arr, k))




