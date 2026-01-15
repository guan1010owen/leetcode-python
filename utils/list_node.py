from modules.node import ListNode

def create_node_from_list(lst):
    if not lst:
        return None

    head = ListNode(lst[0])
    current = head

    for item in lst[1:]:
        current.next = ListNode(item)
        current = current.next

    return head

def convert_to_list(list_node):
    target_list = []
    while list_node:
        target_list.append(list_node.val)
        list_node = list_node.next

    return target_list

def print_node_list(head):
    print("=========================")
    while head is not None:
        print(head.val)
        head = head.next

    print("=========================")