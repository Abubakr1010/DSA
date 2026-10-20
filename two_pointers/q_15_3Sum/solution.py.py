def threeSum(nums: list[int]) -> list[list[int]]:
        
        # --- SOLUTION ---
        n_sort = sorted(nums)
        l = len(n_sort)
        t_sum = []
        
        for i in range(l - 2):
 
            if i > 0 and n_sort[i] == n_sort[i - 1]:
                continue
                
            j = i + 1
            k = l - 1
            
            while j < k:
                current_sum = n_sort[i] + n_sort[j] + n_sort[k]
                
                if current_sum == 0:
                    t_sum.append([n_sort[i], n_sort[j], n_sort[k]])
                    

                    while j < k and n_sort[j] == n_sort[j + 1]:
                        j += 1

                    while j < k and n_sort[k] == n_sort[k - 1]:
                        k -= 1
                        
                    j += 1
                    k -= 1
                elif current_sum > 0:
                    k -= 1
                else:
                    j += 1
                    
        return t_sum

        # --- TIME COMPLEXITY ---
        # O(N2) becaouse of nested loop

        # --- SPACE COMPLEXITY ---
        # O(N) depends on number of 3_sum lists





                



