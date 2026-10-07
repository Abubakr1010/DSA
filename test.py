
def longestConsecutive(nums: list[int]) -> int:

        s = set(nums)
        longest = 0


        for n in s:
          if (n-1) not in s:
               current_num = n
               current_streak = 1

               while (current_num + 1) in s:
                    current_num += 1
                    current_streak += 1
                    longest = max(longest, current_streak)
              

        return longest
    

    


longestConsecutive([100,101,1,3])