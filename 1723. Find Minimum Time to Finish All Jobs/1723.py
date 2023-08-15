from typing import List

class Solution:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        workers = [0] * k
        self.res = float('inf')
        jobs.sort(reverse=True)
        self.start = 0

        def dfs(curr):
            self.start += 1
            if curr == len(jobs):
                self.res = min(self.res, max(workers))
                return
            
            visited = set()
            for i in range(self.start, self.start + k):
                i %= k
                if workers[i] in visited:
                    continue
                if workers[i] + jobs[curr] >= self.res:
                    continue
                visited.add(workers[i])
                workers[i] += jobs[curr]
                dfs(curr + 1)
                workers[i] -= jobs[curr]
        
        dfs(0)
        return self.res


if __name__ == "__main__":
    s = Solution()
    print(s.minimumTimeRequired([1,2,4,7,8], 2))