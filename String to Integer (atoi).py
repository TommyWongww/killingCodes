# @Time    : 2019/8/14 21:04
# @Author  : shakespere
# @FileName: String to Integer (atoi).py
'''
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.
'''
import sys
class Solution(object):
    def myAtoi(self, str):
        INT_MAX = 2147483647
        INT_MIN = -2147483647

        sum = 0
        sign = 1
        i = 0
        if str == '':
            return 0
        while i < len(str) and str[i].isspace():
            i +=1
        if i < len(str) and str[i]=='-':
            sign = -1
        if i < len(str) and (str[i] == '-' or str[i] == '+'):
            i +=1
        while i < len(str) and str[i].isdigit():
            digit = int(str[i])
            if INT_MAX / 10 >= sum:
                sum *=10
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            if INT_MAX - digit >= sum:
                sum += digit
            else:
                if sign == 1:
                    return INT_MAX
                else:
                    return INT_MIN
            i +=1
        return sum*sign

# str =input()
# print(Solution().myAtoi(str))