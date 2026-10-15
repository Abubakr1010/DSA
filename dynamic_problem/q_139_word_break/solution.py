def wordBreak(s: str, wordDict) -> bool:


        unique = set(wordDict)
        track = [False] * (len(s)+1)

        # --- BASE CASE ---
        track[0] = True

        # --- SOLUTION ---
        for i in range(1, len(s)+1):
                for j in range(i):
                    if track[j] and s[j:i] in unique:
                           track[i] = True
                           break
        
        return track[len(s)]

        # --- TIME COMPLEXITY ---
        # O(N2) becaouse of nexted looop

        # --- SPACE COMPLEXITY ---
        # O(N) as it track all the strings in s
        # O(N) for unique as it points to unique strings
                                
