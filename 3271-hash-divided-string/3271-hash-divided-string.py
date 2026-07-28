class Solution:
    def stringHash(self, s: str, k: int) -> str:
        result=[]
        for i in range(0,len(s),k):
            char_sum = sum(ord(c) - ord('a') for c in s[i:i + k])
            hashed_char = chr(ord('a') + (char_sum % 26))
            result.append(hashed_char)
        return "".join(result)