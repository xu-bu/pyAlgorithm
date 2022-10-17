import collections
import functools
from typing import List


class Trie:
    #208
    def __init__(self, ch="", end=False):
        self.ch = ch
        self.end = end
        self.children = [0 for _ in range(26)]

    def insert(self, word: str) -> None:
        if (len(word) == 0):
            self.end = True
            return
        index = ord(word[0]) - 97
        if (self.children[index] == 0):
            self.children[index] = Trie(word[0])
        self.children[index].insert(word[1:])

    def search(self, word: str) -> bool:
        if (len(word) == 0):
            if (self.end):
                return True
            else:
                return False
        index = ord(word[0]) - 97
        if (self.children[index] == 0):
            return False
        return self.children[index].search(word[1:])

    def startsWith(self, prefix: str) -> bool:
        if (len(prefix) == 0):
            return True
        index = ord(prefix[0]) - 97
        if (self.children[index] == 0):
            return False
        return self.children[index].startsWith(prefix[1:])

    def longestWordInsert(self,s)->bool:
        index=ord(s[0])-97
        if (len(s) == 1):
            if(self.children[index]==0):
                self.children[index] = Trie(s[0], True)
            return True
        else:
            if (self.children[index] != 0):
                return self.children[index].longestWordInsert(s[1:])
            return False


class Solution:
    #720
    def longestWord(self, words: List[str]) -> str:
        t=Trie()
        ans=""
        # default setting of python sort string: short string at first, if the length is same then follow the lexicographical order
        words.sort(key=lambda item:len(item))
        for each in words:
            if(t.longestWordInsert(each)):
                if(len(each)>len(ans)):
                    ans=each
                else:
                    ans=max(each,ans)
        return ans


if __name__ == '__main__':
    solution = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(solution.longestWord(words))
