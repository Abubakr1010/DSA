#Given a string s, rearrange the characters of s so that any two adjacent characters are not the same.
#Return any possible rearrangement of s or return "" if not possible.



class Solution:
    def reorganizeString(self, s: str) -> str:
        # --- EDGE CASES ---
        # if empty string -> return empty ""
        # if one charachter -> return empty ""

        # --- IMPLEMENTATION ---

        if not s:
            return ""
        
        if len(s) == 1:
            return (s)
       
        count = Counter(s)

        max_heap = [(-freq, char) for char, freq in count.items()]
        heapq.heapify(max_heap)

        prev_freq, prev_char = 0 , ""
        result = []

        while max_heap:
            freq, char = heapq.heappop(max_heap)
            result.append(char)

            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_char))

            freq += 1
            prev_freq, prev_char = freq, char
        
        result_str = "".join(result)
        return result_str if len(result_str) == len(s) else ""

        # --- TIME COMPEXITY ---
        # O(N)

        # --- TIME COMPEXITY ---
        # O(N)









        
        