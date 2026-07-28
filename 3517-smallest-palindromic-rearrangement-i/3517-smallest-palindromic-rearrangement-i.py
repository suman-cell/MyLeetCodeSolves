class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n=len(s)
        half_len=n//2
        half=sorted(s[:half_len])
        mid =s[half_len] if n%2!=0 else ""
        return "".join(half) + mid + "".join(reversed(half))