class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

def createLinkedList(linked_data):
    reverse_data = linked_data[::-1]
    curr_node, prev_node = ListNode(reverse_data[0]), None
    for i in reverse_data[1:]:
        curr_node, prev_node = ListNode(i, curr_node), curr_node
    head = curr_node
    return head

def printLinkedList(head):
    ans = []
    while head is not None:
        ans.append(head.val)
        head = head.next
    return ans


class TreeNode():
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def createTree(nodeList, index):
    root = TreeNode(nodeList[index])
    
    if 2 * index + 1 < len(nodeList):
        root.left = createTree(nodeList, 2 * index + 1)
    if 2 * index + 2 < len(nodeList):
        root.right = createTree(nodeList, 2 * index + 2)
        
    return root

# nodeList = [1,2,3,None,4,None,5]
# root = createTree(nodeList, 0)