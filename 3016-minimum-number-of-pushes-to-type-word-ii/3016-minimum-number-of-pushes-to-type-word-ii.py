class Solution:
    def minimumPushes(self, word: str) -> int:
        counts = Counter(word)
        sorted_freqs = sorted(counts.values(), reverse=True)
        
        total_pushes = 0
        for i, freq in enumerate(sorted_freqs):
            pushes = (i // 8) + 1
            total_pushes += freq * pushes
            
        return total_pushes