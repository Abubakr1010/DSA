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

#905. Sort Array By Parity
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            if nums[left] % 2 > nums[right] % 2:
                nums[left],nums[right] = nums[right],nums[left]
            if nums[left] % 2 == 0:
                left += 1
            if nums[right] % 2 == 1:
                right -= 1
        return (nums)



# 917. Reverse Only Letters
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if not s[left].isalpha():
                left +=1
            elif not s[right].isalpha():
                right -= 1
            else:
                s[left],s[right]=s[right][left]
                left += 1
                right -= 1
        return ''.join(s)

# 922. Sort Array By Parity II

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        left = 0
        right = 1
        n = len(nums)

        while left < n and right < n:
            if nums[left] %2 == 0:
                left += 2
            elif nums[right] % 2 == 1:
                right += 2
            else:
                nums[left],nums[right] = nums[right],nums[left]
        return (nums)


# 977. Squares of a Sorted Array
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0] * n
        left, right = 0, n-1
        index = n-1

        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2

            if left_square > right_square:
                result[index] = left_square
                left +=1
            else:
                result[index] = right_square
                right -= 1

            index -= 1
            
        return result



