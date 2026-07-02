# Problem: 3826. Find a Safe Walk Through a Grid
# Difficulty: Medium
# Language: Python

from collections import deque
class Solution:
    def findSafeWalk(self, grid: list[list[int]], health: int) -> bool:
        m = len(grid)
        n = len(grid[0])
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        start_health = health - grid[0][0]
        if start_health <= 0:
            return False
        q = deque([(0, 0, start_health )])
        best = [[-1] * n for _ in range(m)]
        best[0][0] = start_health
        
        while q:
            x,y,h = q.popleft()

            if x == m -1 and y == n-1:
                return True

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                
                if 0 <= nx < m and 0 <= ny <n:

                    new_health = h - grid[nx][ny]

                    if new_health > 0 and new_health > best[nx][ny]:
                        best[nx][ny] = new_health
                        q.append((nx, ny, new_health))
        return False
