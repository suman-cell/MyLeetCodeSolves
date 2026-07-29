class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        n = len(s)
        half_len = n // 2
        freq = Counter(s)
        mid_char = ""
        half_freq = {}
        for char, count in freq.items():
            if count % 2 == 1:
                mid_char = char
            half_freq[char] = count // 2
        
        def num_permutations(counts, remaining_len):
            total = 1
            cur_len = remaining_len
            for c, cnt in counts.items():
                if cnt > 0:
                    total *= math.comb(cur_len, cnt)
                    cur_len -= cnt
                    if total >= k:
                        return k
            return total
        res_half = []
        counts = half_freq.copy()
        
        for i in range(half_len):
            placed = False
            remaining_len = half_len - 1 - i
            
            for char in sorted(counts.keys()):
                if counts[char] > 0:
                    counts[char] -= 1
                    ways = num_permutations(counts, remaining_len)
                    
                    if ways >= k:
                        res_half.append(char)
                        placed = True
                        break
                    else:
                        k -= ways
                        counts[char] += 1  
                        
            if not placed:
                return ""

        left_str = "".join(res_half)
        right_str = left_str[::-1]
        
        return left_str + mid_char + right_str