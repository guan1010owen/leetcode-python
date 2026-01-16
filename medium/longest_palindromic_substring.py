# 给你一个字符串s，找到s中最长的回文子串。
#
# 示例1：
#
# 输入：s = "babad"
# 输出："bab"
# 解释："aba"
# 同样是符合题意的答案。
# 示例2：
#
# 输入：s = "cbbd"
# 输出："bb"
# 原题链接: https://leetcode.cn/problems/longest-palindromic-substring/

def center_expand(left, right, str):
    while left >= 0 and right < len(str) and str[left] == str[right]:
        left -= 1
        right += 1

    return str[left + 1:right]

def longest_palindromic_substring(str):
    max_palindromic = ''
    for index in range(len(str)):
        ji_reverse = center_expand(index, index, str)
        if len(ji_reverse) > len(max_palindromic):
            max_palindromic = ji_reverse
        ou_reverse = center_expand(index, index + 1, str)
        if len(ou_reverse) > len(max_palindromic):
            max_palindromic = ou_reverse

    print("%s的最大回文子串为%s" % (str, max_palindromic))
    return max_palindromic


def main():
    s1 = "babad"
    s2 = "cbbd"
    s3 = "hookaaakooh"

    longest_palindromic_substring(s1)
    longest_palindromic_substring(s2)
    longest_palindromic_substring(s3)

if __name__ == '__main__':
    main()