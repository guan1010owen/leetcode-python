# 给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储
# 一位数字。
#
# 请你将两个数相加，并以相同形式返回一个表示和的链表。
# 你可以假设除了数字0之外，这两个数都不会以0开头。
#
# 示例
# 1：
#
# 输入：l1 = [2, 4, 3], l2 = [5, 6, 4]
# 输出：[7, 0, 8]
# 解释：342 + 465 = 807.
# 示例
# 2：
#
# 输入：l1 = [0], l2 = [0]
# 输出：[0]
# 示例
# 3：
#
# 输入：l1 = [9, 9, 9, 9, 9, 9, 9], l2 = [9, 9, 9, 9]
# 输出：[8, 9, 9, 9, 0, 0, 0, 1]
#
# 提示：
#
# 每个链表中的节点数在范围[1, 100]
# 内
# 0 <= Node.val <= 9
# 题目数据保证列表表示的数字不含前导零

# 原题目链接：https://leetcode.cn/problems/add-two-numbers/

from modules.node import ListNode


# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:

    dummyhead = ListNode(0)
    current = dummyhead
    carry = 0

    while l1 is not None or l2 is not None:
        var1 = l1.val if l1 is not None else 0
        var2 = l2.val if l2 is not None else 0

        sum = var1 + var2 + carry

        carry = sum // 10
        current.next = ListNode(sum % 10)

        if l1 is not None:
            l1 = l1.next
        if l2 is not None:
            l2 = l2.next

        if carry > 0:
            current.next = ListNode(carry)

        return dummyhead.next


def main():
    l1 = ListNode(1)
    l2 = ListNode(2)

if __name__ == '__main__':
    main()