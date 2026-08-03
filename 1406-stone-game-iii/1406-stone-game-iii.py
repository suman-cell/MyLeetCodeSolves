class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
       
        dp1 = dp2 = dp3 = 0  
        
        for i in range(n - 1, -1, -1):
            curr_sum = 0
            max_diff = float('-inf')
            
            
            for k in range(1, 4):
                if i + k <= n:
                    curr_sum += stoneValue[i + k - 1]
                    
                    
                    next_dp = dp1 if k == 1 else (dp2 if k == 2 else dp3)
                    
                    max_diff = max(max_diff, curr_sum - next_dp)
            
            
            dp3 = dp2
            dp2 = dp1
            dp1 = max_diff

        
        alice_diff = dp1
        
        if alice_diff > 0:
            return "Alice"
        elif alice_diff < 0:
            return "Bob"
        else:
            return "Tie"