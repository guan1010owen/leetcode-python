# 给定一个字符串s ，请你找出其中不含有重复字符的最长子串的长度。
#
# 示例
# 1: 输入: s = "abcabcbb"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"abc"，所以其长度为3。注意"bca"和"cab"也是正确答案。
# 示例2:输入: s = "bbbbb"
# 输出: 1
# 解释: 因为无重复字符的最长子串是"b"，所以其长度为1。
# 示例3:输入: s = "pwwkew"
# 输出: 3
# 解释: 因为无重复字符的最长子串是"wke"，所以其长度为3。
# 请注意，你的答案必须是子串的长度，"pwke"是一个子序列，不是子串。

def longest_sub_string(str):
    left = 0
    max_length = 0
    target_set = set()
    sub_strs = []

    for right in range(len(str)):
        while(str[right] in target_set):
            target_set.remove(str[left])
            left += 1

        target_set.add(str[right])
        if right - left + 1 == max_length and str[left:right + 1] not in sub_strs:
            sub_strs.append(str[left:right + 1])

        if right - left + 1 > max_length and str[left:right + 1] not in sub_strs:
            sub_strs.clear()
            sub_strs.append(str[left:right + 1])

        max_length = max(max_length, right - left + 1)

    print("%s的无重复最大子串有%s,长度为%d" % (str, ", ".join(sub_strs), max_length))
    return max_length


def main():
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwke"

    longest_sub_string(s1)
    longest_sub_string(s2)
    longest_sub_string(s3)

if __name__ == '__main__':
    main()