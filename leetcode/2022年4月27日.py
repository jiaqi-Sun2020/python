heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
visted = set()
def search_(x,y):
    if x==m-1 or y==n-1:
        return False
    nowplace = hashmap[(x, y)]
    down = hashmap[(x,y+1)]
    right = hashmap[(x+1,y)]
    if nowplace>down and nowplace> right:
        return x,y
    else:
        if hashmap[(x,y)]<=hashmap[(x+1,y)]:
            return search_(x+1,y)
        if hashmap[(x,y)]<=hashmap[(x,y+1)]:
            return search_(x,y+1)




m = len(heights)
n = len(heights[0])
hashmap = {}
for x in range(m):
    for y in range(n):
        hashmap[(x,y)]=heights[x][y]

list__ = []
for i in range(m):
    list__.append(search_(i,0))
for t in range(n):
    list__.append(search_(0,t))

print(list__)


"""
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m, n = len(heights), len(heights[0])

        def search(starts: List[Tuple[int, int]]) -> Set[Tuple[int, int]]:
            visited = set()
            def dfs(x: int, y: int):
                if (x, y) in visited:
                    return
                visited.add((x, y))
                for nx, ny in ((x, y + 1), (x, y - 1), (x - 1, y), (x + 1, y)):
                    if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] >= heights[x][y]:
                        dfs(nx, ny)
            for x, y in starts:
                dfs(x, y)
            return visited

        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]
        return list(map(list, search(pacific) & search(atlantic)))



"""