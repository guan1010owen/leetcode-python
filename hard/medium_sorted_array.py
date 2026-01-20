'''
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。
算法的时间复杂度应该为 O(log (m+n)) 。

示例 1：

输入：nums1 = [1,3], nums2 = [2]
输出：2.00000
解释：合并数组 = [1,2,3] ，中位数 2
示例 2：

输入：nums1 = [1,2], nums2 = [3,4]
输出：2.50000
解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5

提示：

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106

原题链接：https://leetcode.cn/problems/median-of-two-sorted-arrays/description/
'''

import sys
def find_medium_sorted_array(num_lst1, num_lst2):
    if len(num_lst1) > len(num_lst2):
        num_lst1, num_lst2 = num_lst2, num_lst1

    m,n = len(num_lst1), len(num_lst2)
    half = (m + n)//2

    left, right = 0, m

    while left <= right:
        pos1 = (left + right)//2
        pos2 = half - pos1

        lst1_left_max = -sys.maxsize if pos1 == 0 else num_lst1[pos1 - 1]
        lst1_right_min = sys.maxsize if pos1 == m else num_lst1[pos1]

        lst2_left_max = -sys.maxsize if pos2 == 0 else num_lst2[pos2 - 1]
        lst2_right_min = sys.maxsize if pos2 == n else num_lst2[pos2]

        if lst1_left_max <= lst2_right_min and lst2_left_max <= lst1_right_min:
            if (m + n) %2 == 0:
                left_max = max(lst1_left_max, lst2_left_max)
                right_min = min(lst1_right_min, lst2_right_min)

                return (left_max + right_min)/2.0
            else:
                return min(lst1_right_min, lst2_right_min)

        elif lst1_left_max > lst2_right_min:
            right = pos1 - 1
        else:
            left = pos1 + 1

def main():
    nums1 = [1,3]
    nums2 = [2]

    nums3 = [1,2]
    nums4 = [3,4]

    print(find_medium_sorted_array(nums1, nums2))
    print(find_medium_sorted_array(nums3, nums4))

if __name__ == '__main__':
    main()