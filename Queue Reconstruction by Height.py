# @Time    : 2019/4/22 22:57
# @Author  : shakespere
# @FileName: Queue Reconstruction by Height.py
'''
406. Queue Reconstruction by Height
Medium
Suppose you have a random list of people standing in a queue. Each person is described by a pair of integers (h, k), where h is the height of the person and k is the number of people in front of this person who have a height greater than or equal to h. Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.


Example

Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
'''
class Solution(object):
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        people.sort(key = lambda x:(-x[0],x[1])) #取负号让其递减排序，相等根据第二个递增排序
        res = []
        for i in people:
            res.insert(i[1],i)#排好序后，根据第二个位置进行重新插入即可
        return res