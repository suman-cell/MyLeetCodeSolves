class Solution:
    def remainingMethods(self, n: int, k: int, invocations: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        for u, v in invocations:
            adj[u].append(v)
            
        
        suspicious = set([k])
        queue = deque([k])
        
        while queue:
            node = queue.popleft()
            for neighbor in adj[node]:
                if neighbor not in suspicious:
                    suspicious.add(neighbor)
                    queue.append(neighbor)
                    
        
        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))
                
        
        return [i for i in range(n) if i not in suspicious]