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

def find_medium_sorted_array(num_lst1, num_lst2):
    merged_lst = num_lst1 + num_lst2
    sorted_lst = sorted(merged_lst)

    if len(sorted_lst) % 2 == 0:
        center = len(sorted_lst) // 2
        return (sorted_lst[center - 1] + sorted_lst[center])/2.0
    else:
        center = (len(sorted_lst) + 1) // 2
        return sorted_lst[center - 1]/1.0

def main():
    nums1 = [1,3]
    nums2 = [2]

    nums3 = [1,2]
    nums4 = [3,4]

    print(find_medium_sorted_array(nums1, nums2))
    print(find_medium_sorted_array(nums3, nums4))

if __name__ == '__main__':
    main()