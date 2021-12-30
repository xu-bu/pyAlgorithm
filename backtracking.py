class Solution(object):
    #含重复元素的顺序全子集，由于多个子集在sort之后会相同，所以需要去重
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

    #78 不含重复元素的全子集
    def subsets(self, nums):
        ans = []
        item = []
        n=len(nums)
        def backtrack(i):
            #每个位置都可以选或者不选，遍历完之后将item放入ans
            if i == n:
                ans.append(item[:])
            else:
                item.append(nums[i])
                backtrack(i + 1)
                item.pop()
                backtrack(i + 1)

        backtrack(0)
        return ans

    #17 本题用回溯和用暴力效率一样，参考意义不大
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

    #46 以[1,2,3]为例,如果使用暴力法，会出现[1,1,1]的情况，复杂度为n^n，而回溯法的复杂度是全排列的数量，为n!

    #22 含重复元素的全排，
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        item=[]
        def backtrack(i):
            if i==n*2:
                ans.append(item)
            else:




if __name__ == '__main__':
    s=Solution()
    nums="23"
    print(s.letterCombinations(nums))
