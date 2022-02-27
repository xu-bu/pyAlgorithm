import collections


class Solution(object):
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
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]) or board[i][j] != word[k]:
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
