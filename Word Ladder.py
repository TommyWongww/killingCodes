# @Time    : 2019/8/23 9:45
# @Author  : shakespere
# @FileName: Word Ladder.py
'''
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
'''

import collections
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordset = set(wordList)
        bfs = collections.deque()
        bfs.append((beginWord,1))
        while bfs:
            word,length = bfs.popleft()
            if word == endWord:
                return length
            for i in range(len(word)):
                for c in "abcdefghijklmnopqrstuvwxyz":
                    newword = word[:i]+c+word[i+1:]
                    if newword in wordset and newword!=word:
                        wordset.remove(newword)
                        bfs.append((newword,length+1))
        return 0
# b = input()
# e = input()
# wordList = input().strip().split(',')
# print(Solution().ladderLength(b,e,wordList))
