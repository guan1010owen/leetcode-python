'''
给你一个整数 x ，如果 x 是一个回文整数，返回 true ；否则，返回 false 。
回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。
例如，121 是回文，而 123 不是。

示例 1：
输入：x = 121
输出：true

示例 2：
输入：x = -121
输出：false
解释：从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。

示例 3：
输入：x = 10
输出：false
解释：从右向左读, 为 01 。因此它不是一个回文数。
原题链接：https://leetcode.cn/problems/palindrome-number/description/
'''


def palindromic_number(x):
    if x < 0:
        return False

    number = str(x)
    head = 0
    tail = -1

    while head < (len(number) + 1)/2:
        if number[head] != number[tail]:
            return False
        head += 1
        tail -= 1

    return True

def main():
    num1 = 121
    num2 = -121

    print(palindromic_number(num1))
    print(palindromic_number(num2))

if __name__ == '__main__':
    main()