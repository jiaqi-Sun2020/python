"""
一只猫和一只老鼠在玩一个叫做猫和老鼠的游戏。

它们所处的环境设定是一个 rows x cols 的方格 grid ，其中每个格子可能是一堵墙、一块地板、一位玩家（猫或者老鼠）或者食物。

玩家由字符 'C' （代表猫）和 'M' （代表老鼠）表示。
地板由字符 '.' 表示，玩家可以通过这个格子。
墙用字符 '#' 表示，玩家不能通过这个格子。
食物用字符 'F' 表示，玩家可以通过这个格子。
字符 'C' ， 'M' 和 'F' 在 grid 中都只会出现一次。
猫和老鼠按照如下规则移动：

老鼠 先移动 ，然后两名玩家轮流移动。
每一次操作时，猫和老鼠可以跳到上下左右四个方向之一的格子，他们不能跳过墙也不能跳出 grid 。
catJump 和 mouseJump 是猫和老鼠分别跳一次能到达的最远距离，它们也可以跳小于最大距离的长度。
它们可以停留在原地。
老鼠可以跳跃过猫的位置。
游戏有 4 种方式会结束：

如果猫跟老鼠处在相同的位置，那么猫获胜。
如果猫先到达食物，那么猫获胜。
如果老鼠先到达食物，那么老鼠获胜。
如果老鼠不能在 1000 次操作以内到达食物，那么猫获胜。
给你 rows x cols 的矩阵 grid 和两个整数 catJump 和 mouseJump ，双方都采取最优策略，如果老鼠获胜，那么请你返回 true ，否则返回 false 。

 

示例 1：



输入：grid = ["####F","#C...","M...."], catJump = 1, mouseJump = 2
输出：true
解释：猫无法抓到老鼠，也没法比老鼠先到达食物。
示例 2：



输入：grid = ["M.C...F"], catJump = 1, mouseJump = 4
输出：true
示例 3：

输入：grid = ["M.C...F"], catJump = 1, mouseJump = 3
输出：false
示例 4：

输入：grid = ["C...#","...#F","....#","M...."], catJump = 2, mouseJump = 5
输出：false
示例 5：

输入：grid = [".M...","..#..","#..#.","C#.#.","...#F"], catJump = 3, mouseJump = 1
输出：true
 

提示：

rows == grid.length
cols = grid[i].length
1 <= rows, cols <= 8
grid[i][j] 只包含字符 'C' ，'M' ，'F' ，'.' 和 '#' 。
grid 中只包含一个 'C' ，'M' 和 'F' 。
1 <= catJump, mouseJump <= 8

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/cat-and-mouse-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""

#太难了啊---直接cv


MOUSE_TURN = 0
CAT_TURN = 1
UNKNOWN = 0
MOUSE_WIN = 1
CAT_WIN = 2
MAX_MOVES = 1000
DIRS = ((-1, 0), (1, 0), (0, -1), (0, 1))

class Solution:
    def canMouseWin(self, grid: List[str], catJump: int, mouseJump: int) -> bool:
        rows, cols = len(grid), len(grid[0])

        def getPos(row: int, col: int) -> int:
            return row * cols + col

        startMouse = startCat = food = 0
        for i, row in enumerate(grid):
            for j, ch in enumerate(row):
                if ch == 'M':
                    startMouse = getPos(i, j)
                elif ch == 'C':
                    startCat = getPos(i, j)
                elif ch == 'F':
                    food = getPos(i, j)

        # 计算每个状态的度
        total = rows * cols
        degrees = [[[0, 0] for _ in range(total)] for _ in range(total)]
        for mouse in range(total):
            mouseRow, mouseCol = divmod(mouse, cols)
            if grid[mouseRow][mouseCol] == '#':
                continue
            for cat in range(total):
                catRow, catCol = divmod(cat, cols)
                if grid[catRow][catCol] == '#':
                    continue
                degrees[mouse][cat][MOUSE_TURN] += 1
                degrees[mouse][cat][CAT_TURN] += 1
                for dx, dy in DIRS:
                    row, col, jump = mouseRow + dx, mouseCol + dy, 1
                    while 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#' and jump <= mouseJump:
                        nextMouse = getPos(row, col)
                        nextCat = getPos(catRow, catCol)
                        degrees[nextMouse][nextCat][MOUSE_TURN] += 1
                        row += dx
                        col += dy
                        jump += 1
                    row, col, jump = catRow + dx, catCol + dy, 1
                    while 0 <= row < rows and 0 <= col < cols and grid[row][col] != '#' and jump <= catJump:
                        nextMouse = getPos(mouseRow, mouseCol)
                        nextCat = getPos(row, col)
                        degrees[nextMouse][nextCat][CAT_TURN] += 1
                        row += dx
                        col += dy
                        jump += 1

        results = [[[[0, 0], [0, 0]] for _ in range(total)] for _ in range(total)]
        q = deque()

        # 猫和老鼠在同一个单元格，猫获胜
        for pos in range(total):
            row, col = divmod(pos, cols)
            if grid[row][col] == '#':
                continue
            results[pos][pos][MOUSE_TURN][0] = CAT_WIN
            results[pos][pos][MOUSE_TURN][1] = 0
            results[pos][pos][CAT_TURN][0] = CAT_WIN
            results[pos][pos][CAT_TURN][1] = 0
            q.append((pos, pos, MOUSE_TURN))
            q.append((pos, pos, CAT_TURN))

        # 猫和食物在同一个单元格，猫获胜
        for mouse in range(total):
            mouseRow, mouseCol = divmod(mouse, cols)
            if grid[mouseRow][mouseCol] == '#' or mouse == food:
                continue
            results[mouse][food][MOUSE_TURN][0] = CAT_WIN
            results[mouse][food][MOUSE_TURN][1] = 0
            results[mouse][food][CAT_TURN][0] = CAT_WIN
            results[mouse][food][CAT_TURN][1] = 0
            q.append((mouse, food, MOUSE_TURN))
            q.append((mouse, food, CAT_TURN))

        # 老鼠和食物在同一个单元格且猫和食物不在同一个单元格，老鼠获胜
        for cat in range(total):
            catRow, catCol = divmod(cat, cols)
            if grid[catRow][catCol] == '#' or cat == food:
                continue
            results[food][cat][MOUSE_TURN][0] = MOUSE_WIN
            results[food][cat][MOUSE_TURN][1] = 0
            results[food][cat][CAT_TURN][0] = MOUSE_WIN
            results[food][cat][CAT_TURN][1] = 0
            q.append((food, cat, MOUSE_TURN))
            q.append((food, cat, CAT_TURN))

        def getPrevStates(mouse: int, cat: int, turn: int) -> List[Tuple[int, int, int]]:
            mouseRow, mouseCol = divmod(mouse, cols)
            catRow, catCol = divmod(cat, cols)
            prevTurn = CAT_TURN if turn == MOUSE_TURN else MOUSE_TURN
            maxJump = mouseJump if prevTurn == MOUSE_TURN else catJump
            startRow = mouseRow if prevTurn == MOUSE_TURN else catRow
            startCol = mouseCol if prevTurn == MOUSE_TURN else catCol
            prevStates = [(mouse, cat, prevTurn)]
            for dx, dy in DIRS:
                i, j, jump = startRow + dx, startCol + dy, 1
                while 0 <= i < rows and 0 <= j < cols and grid[i][j] != '#' and jump <= maxJump:
                    prevMouseRow = i if prevTurn == MOUSE_TURN else mouseRow
                    prevMouseCol = j if prevTurn == MOUSE_TURN else mouseCol
                    prevCatRow = catRow if prevTurn == MOUSE_TURN else i
                    prevCatCol = catCol if prevTurn == MOUSE_TURN else j
                    prevMouse = getPos(prevMouseRow, prevMouseCol)
                    prevCat = getPos(prevCatRow, prevCatCol)
                    prevStates.append((prevMouse, prevCat, prevTurn))
                    i += dx
                    j += dy
                    jump += 1
            return prevStates

        # 拓扑排序
        while q:
            mouse, cat, turn = q.popleft()
            result = results[mouse][cat][turn][0]
            moves = results[mouse][cat][turn][1]
            for prevMouse, prevCat, prevTurn in getPrevStates(mouse, cat, turn):
                if results[prevMouse][prevCat][prevTurn][0] == UNKNOWN:
                    if result == MOUSE_WIN and prevTurn == MOUSE_TURN or result == CAT_WIN and prevTurn == CAT_TURN:
                        results[prevMouse][prevCat][prevTurn][0] = result
                        results[prevMouse][prevCat][prevTurn][1] = moves + 1
                        q.append((prevMouse, prevCat, prevTurn))
                    else:
                        degrees[prevMouse][prevCat][prevTurn] -= 1
                        if degrees[prevMouse][prevCat][prevTurn] == 0:
                            loseResult = CAT_WIN if prevTurn == MOUSE_TURN else MOUSE_WIN
                            results[prevMouse][prevCat][prevTurn][0] = loseResult
                            results[prevMouse][prevCat][prevTurn][1] = moves + 1
                            q.append((prevMouse, prevCat, prevTurn))
        return results[startMouse][startCat][MOUSE_TURN][0] == MOUSE_WIN and results[startMouse][startCat][MOUSE_TURN][1]<= MAX_MOVES
