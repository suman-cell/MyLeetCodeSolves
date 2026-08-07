class Solution:
    def smallestNumber(self, num: str, t: int) -> str:
        temp_t = t
        counts = {2: 0, 3: 0, 5: 0, 7: 0}
        for p in [2, 3, 5, 7]:
            while temp_t % p == 0:
                counts[p] += 1
                temp_t //= p
        
        if temp_t > 1:
            return "-1"
            
        def get_factors(digit: int):
            f = {2: 0, 3: 0, 5: 0, 7: 0}
            if digit == 2: f[2] = 1
            elif digit == 3: f[3] = 1
            elif digit == 4: f[2] = 2
            elif digit == 5: f[5] = 1
            elif digit == 6: f[2] = 1; f[3] = 1
            elif digit == 7: f[7] = 1
            elif digit == 8: f[2] = 3
            elif digit == 9: f[3] = 2
            return f

        def get_optimal_digits(c2, c3, c5, c7):
            best_digits = None
            for n6 in range(min(c2, c3) + 1):
                rem2 = c2 - n6
                rem3 = c3 - n6
                
                n9 = rem3 // 2
                r3 = rem3 % 2
                
                n8 = rem2 // 3
                r2 = rem2 % 3
                
                n4 = 1 if r2 == 2 else 0
                n2 = 1 if r2 == 1 else 0
                n3 = 1 if r3 == 1 else 0
                
                digits = sorted([9]*n9 + [8]*n8 + [7]*c7 + [6]*n6 + [5]*c5 + [4]*n4 + [3]*n3 + [2]*n2)
                
                if best_digits is None or len(digits) < len(best_digits) or (len(digits) == len(best_digits) and digits < best_digits):
                    best_digits = digits
                    
            return best_digits

        def min_digits_needed(c2, c3, c5, c7):
            return len(get_optimal_digits(c2, c3, c5, c7))

        def fill_suffix(req2, req3, req5, req7, length):
            digits = get_optimal_digits(req2, req3, req5, req7)
            if len(digits) > length:
                return None
            return "".join(map(str, [1] * (length - len(digits)) + digits))

        n = len(num)
        
        first_zero = num.find('0')
        limit = first_zero if first_zero != -1 else n
        
        pref_factors = [{2: 0, 3: 0, 5: 0, 7: 0} for _ in range(n + 1)]
        for i in range(limit):
            d = int(num[i])
            f = get_factors(d)
            for p in [2, 3, 5, 7]:
                pref_factors[i + 1][p] = pref_factors[i][p] + f[p]

        if first_zero == -1:
            rem2 = max(0, counts[2] - pref_factors[n][2])
            rem3 = max(0, counts[3] - pref_factors[n][3])
            rem5 = max(0, counts[5] - pref_factors[n][5])
            rem7 = max(0, counts[7] - pref_factors[n][7])
            if rem2 == rem3 == rem5 == rem7 == 0:
                return num

        for i in range(limit, -1, -1):
            start_d = int(num[i]) + 1 if i < n else 1
            for d in range(start_d, 10):
                f = get_factors(d)
                rem2 = max(0, counts[2] - pref_factors[i][2] - f[2])
                rem3 = max(0, counts[3] - pref_factors[i][3] - f[3])
                rem5 = max(0, counts[5] - pref_factors[i][5] - f[5])
                rem7 = max(0, counts[7] - pref_factors[i][7] - f[7])
                
                rem_len = n - 1 - i
                if min_digits_needed(rem2, rem3, rem5, rem7) <= rem_len:
                    suf = fill_suffix(rem2, rem3, rem5, rem7, rem_len)
                    if suf is not None:
                        return num[:i] + str(d) + suf

        target_len = n + 1
        while True:
            if min_digits_needed(counts[2], counts[3], counts[5], counts[7]) <= target_len:
                suf = fill_suffix(counts[2], counts[3], counts[5], counts[7], target_len)
                if suf is not None:
                    return suf
            target_len += 1