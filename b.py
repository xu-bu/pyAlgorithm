import collections
import heapq
from typing import List
import string


class Solution:
    def distinctNames(self, ideas: List[str]) -> int:
        n=len(ideas)
        #cnt[i][j]表示将首字母chr(i)改为chr(j)之后能产生多少种答案
        #过程：ideas = ["coffee","donuts","time","toffee"]为例
        #从第一个单词开始，先算i=2，然后j遍历26，首先j为0的时候，单词变为aoffee，这是可行的，cnt[2][0]+=1，而当j=2时，单词变为coffee，在ideas中出现过了，所以不行
        #完成这个过程后，分别对i，j遍历26，每一次都是ans+=cnt[i][j]*cnt[j][i]
        cnt=[[0 for i in range(26)]for j in range(26)]
        # dic=collections.defaultdict(list)
        ans=0
        dic={}
        for each in ideas:
            dic[each]=1
        for each in ideas:
            for j in range(26):
                new=string.ascii_lowercase[j]+each[1:]
                if dic.get(new,0)==0:
                    cnt[ord(each[0])-ord('a')][j]+=1
        for i in range(26):
            for j in range(26):
                ans+=cnt[i][j]*cnt[j][i]
        return ans


if __name__ == '__main__':
    solution=Solution()
    ideas = ["coffee","donuts","time","toffee"]
    print(solution.distinctNames(ideas))