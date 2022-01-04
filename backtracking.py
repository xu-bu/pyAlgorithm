class Solution(object):
    #回溯法主要用于解决需要输出所有结果的排列组合与子集问题

    #17 本题只是为了说明回溯法的思想和基本框架，但事实上用回溯和用暴力效率一样，参考意义不大
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        n=len(digits)
        ans=[]

        if  n== 0:
            return []
        phoneMap = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        def backtrack(i,item):
            #回溯digits[i],所以递归出口是i==n
            if i==n:
                ans.append("".join(item))
            else:
                digit=digits[i]
                for ch in phoneMap[digit]:
                    item.append(ch)
                    backtrack(i+1,item)
                    #以“123”为例，此时的情况是以ad开头的所有情况都回溯完了，然后把d pop掉，进入下一轮循环，append(e)进来，然后回溯ae开头的情况
                    item.pop()
        backtrack(0,[])
        return ans

    # 78 不含重复元素的全子集
    def subsets(self, nums):
        ans = []
        item = []
        n = len(nums)

        def backtrack(i):
            # 每个位置都可以选或者不选，遍历完之后将item放入ans
            if i == n:
                ans.append(item[:])
            else:
                item.append(nums[i])
                backtrack(i + 1)
                item.pop()
                backtrack(i + 1)

        backtrack(0)
        return ans

    #90 含重复元素的顺序全子集，由于多个子集在sort之后会相同，所以需要去重
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)
        def backtrack(item,i):
            #i代表插入nums[i],所以递归出口是i>=n，但是要注意出口只需要return，因为对于全集，其过程是先item.append最后一个元素，然后ans.append(item)，然后再backtrack进入到递归出口
            if i>=n:
                return
            #一定要先忘item里面加，再往ans里面加。注意ans.append时要append深拷贝，不然随着item在之后的回溯中发生变化，ans中的item也会变
            item.append(nums[i])
            if sorted(item) not in ans:
                ans.append(sorted(item)[:])
            backtrack(item,i+1)
            item.pop()
            backtrack(item,i+1)
        backtrack([],0)
        ans.append([])
        return ans

    #22 从小列表中选元素生成短长度n的全排列
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        item = []
        chs = ['(', ')']
        self.l = self.r = 0

        def backtrack(k):
            if len(item) == 2 * n:
                temp = "".join(item)
                if temp and self.l == self.r:
                    ans.append(temp)
                return
            for i in chs:
                if self.r > self.l:
                    continue
                if i == '(':
                    self.l += 1
                else:
                    self.r += 1
                item.append(i)
                backtrack(k + 1)
                if item.pop() == '(':
                    self.l -= 1
                else:
                    self.r -= 1

        backtrack(0)
        return ans

    #77 Cnk 从无重复元素长度为n的大列表中取k个元素出来做组合（结果有序）。然后39
    def combine(self,nums,k):
        n=len(nums)
        ans=[]
        item=[]
        def backtrack(i):
            if len(item)==k:
                ans.append(item[:])
                return
            for j in range(i,n):
                item.append(nums[j])
                #注意这里是j+1不是i+1
                backtrack(j+1)
                item.pop()
        backtrack(0)
        return ans

    #39 可重复选元素的组合，但是这个题和40用dfs的回溯更好
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        ans = []
        item = []
        n = len(candidates)

        def backtrack(i):
            s = sum(item)
            if s == target:
                temp = sorted(item)
                if temp not in ans:
                    ans.append(temp)
                return
            elif s > target:
                return
            for j in range(n):
                item.append(candidates[j])
                backtrack(i + 1)
                item.pop()

        backtrack(0)
        return ans

    #40 含重复元素的列表中选部分出来组合+剪枝，也是用dfs回溯更好
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        ans = []
        item = []
        n = len(candidates)

        def backtrack(i):
            s = sum(item)
            if s == target:
                #有重复元素，所以需要去重
                temp = sorted(item)
                if temp not in ans:
                    ans.append(temp)
                return
            elif s > target:
                return

            for j in range(i, n):
                #剪枝
                if candidates[j] > target:
                    return
                if j > i and candidates[j] == candidates[j - 1]:
                    continue
                item.append(candidates[j])
                backtrack(j + 1)
                item.pop()

        backtrack(0)
        return ans

    # 46，47 全排列（含或不含重复元素均可），核心思想在于使用verdict数组判断元素是否已使用
    # 以[1,2,3]为例,如果使用暴力法，会出现[1,1,1]的情况，复杂度为n^n，而回溯法的复杂度是全排列的数量，为n!
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans = []
        item = []
        n = len(nums)
        # 利用verdict判断该元素是否使用过，用0，1也行，因为python的int和bool型大小一样
        verdict = [False] * n

        def backtrack():
            # 这里必须是len(item)，由于递归出口改变了，所以backtrack不需要形参了
            if len(item) == n:
                if item not in ans:
                    ans.append(item[:])
                return
            for i in range(n):
                if verdict[i]:
                    continue
                item.append(nums[i])
                verdict[i] = True
                backtrack()
                item.pop()
                verdict[i] = False

        backtrack()
        return ans



if __name__ == '__main__':
    s=Solution()
    nums="23"
    print(s.letterCombinations(nums))
