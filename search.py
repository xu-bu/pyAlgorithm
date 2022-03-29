import collections


class Solution(object):
    #200图中搜索岛屿数量
    def numIslands(self, grid: list[list[str]]) -> int:
        #dfs整体结构：
        #dfs先写出口，对四个不同方向for循环，满足条件就开始搜索
        #主函数两轮循环遍历，满足条件则开始搜索，搜完岛屿数量加一
        rows, columns = len(grid), len(grid[0])
        ans = 0

        def dfs(i, j):
            #递归出口，如果不是1，说明要么是0，没有岛屿，要么是.，已经被搜索过了
            if grid[i][j] != '1':
                return
            grid[i][j] = '.'
            for (x, y) in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                #不要用range去判断，很慢
                if 0 <= x < rows and 0 <= y < columns:
                    dfs(x, y)

        for i in range(rows):
            for j in range(columns):
                if grid[i][j] == '1':
                    #一轮搜索可以搜完一整个孤岛，再开启下一次搜索的时候已经是下一个岛了
                    dfs(i, j)
                    ans += 1
        return ans

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        rows,columns=len(board),len(board[0])
        n=len(word)
        if n>rows*columns:
            return False

        def dfs(i,j,k):
            if not 0 <= i < rows or not 0 <= j < columns or board[i][j] != word[k]:
                return False
            #加等号解决word是一个字母的情况
            if k >= n-1:
                return True
            temp=board[i][j]
            board[i][j]=' '
            res = dfs(i + 1, j, k + 1) or dfs(i - 1, j, k + 1) or dfs(i, j + 1, k + 1) or dfs(i, j - 1, k + 1)
            board[i][j]=temp
            return res


        for i in range(rows):
            for j in range(columns):
                if board[i][j]==word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

    #207 判断有向图中有无环
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        #0表示未开始，1表示搜索中，2表示已完成
        verdict=[0]*numCourses
        dic=collections.defaultdict(list)
        for each in prerequisites:
            dic[each[0]].append(each[1])
        #课程c是否可学
        def dfs(c):
            if verdict[c]==2:
                return True
            elif verdict[c]==1:
                return False
            verdict[c]=1
            for preCourse in dic[c]:
                if verdict[preCourse]==2:
                    continue
                if not dfs(preCourse):
                    return False
            verdict[c]=2
            return True


        for each in prerequisites:
            if verdict[each[0]]==2:
                continue
            if not dfs(each[0]):
                return False
        return True

if __name__ == '__main__':
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"

    solution=Solution()
    print(solution.exist(board,word))