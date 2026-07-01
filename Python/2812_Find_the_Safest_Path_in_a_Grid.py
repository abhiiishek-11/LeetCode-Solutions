# Problem: 2812. Find the Safest Path in a Grid
# Difficulty: Medium
# Language: Python

from collections import deque
class Solution:
    def maximumSafenessFactor(self, grid: list[list[int]]) -> int:
        n = len(grid)
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        dist = [[-1]*n for _ in range(n)]
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))
        while q:
            x,y = q.popleft()
            for dx,dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and dist [nx][ny] == -1:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
        def canReach(limit):
            if dist[0][0] < limit:
                return False
            
            visited = [[False] * n for _ in range(n)]
            q = deque([(0, 0)])
            visited[0][0] = True

            while q:
                x, y = q.popleft()

                if x == n-1 and y == n-1:
                    return True

                for dx, dy in directions:
                    nx, ny = x + dx, y+ dy

                    if (
                        0 <= nx < n and 
                        0 <= ny < n and
                        not visited[nx][ny] and 
                        dist[nx][ny] >= limit
                    ):
                        visited[nx][ny] = True
                        q.append((nx, ny))
            return False

        left, right = 0, max(max(row) for row in dist)
        answer = 0
        while left <= right:
            mid = (left + right) // 2
            if canReach(mid):
                answer = mid
                left = mid + 1
            else:
                right = mid - 1

        return answer