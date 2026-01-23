'''
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围 [−231,  231 − 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。

示例 1：
输入：x = 123
输出：321

示例 2：
输入：x = -123
输出：-321

示例 3：
输入：x = 120
输出：21

示例 4：
输入：x = 0
输出：0

原题链接：https://leetcode.cn/problems/reverse-integer/
'''


def reverse_integer(x):

    temp = x

    if x == 0:
        return 0

    negative = 1 if x < 0 else 0

    splits = []
    num = 0

    if negative:
        temp = -temp

    while temp != 0:

        result = temp % 10
        splits.append(result)
        temp = temp // 10

    splits.reverse()
    for index in range(len(splits)):
        num += splits[index] * pow(10, index)

    if num > pow(2, 31) - 1:
        return 0

    return -num if negative else num


'''this function seems not work in python, a%b function works different in
python when a is negative'''
def reverse_integer_2(x):
    result = 0

    while x != 0:
        temp = x % 10

        if (result > pow(2 ,31) - 1 or result < -pow(2 ,31)):
            return 0

        result = result*10 + temp
        x //= 10

    return result

def main():
    x1 = 123
    x2 = -123
    x3 = 120
    x4 = 1005
    x5 = 1534236469

    print(reverse_integer(x1))
    print(reverse_integer(x2))
    print(reverse_integer(x3))
    print(reverse_integer(x4))
    print(reverse_integer(x5))

if __name__ == '__main__':
    main()