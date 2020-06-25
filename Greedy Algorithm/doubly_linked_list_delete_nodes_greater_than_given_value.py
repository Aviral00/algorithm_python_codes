class Node:

    def __init__(self, key):
        self.key = key
        self.left = self.right = None


def dll(head, node):

    if head is None:
        head = node

    else:
        temp = head
        while temp.right is not None:
            temp = temp.right
        temp.right = node
        node.left = temp


def print_dll(head):

    if head is not None:
        temp = head
        while temp is not None:
            print(temp.key)
            temp = temp.right


head = Node(1)
dll(head, Node(2))
dll(head, Node(3))
dll(head, Node(4))
dll(head, Node(5))
dll(head, Node(6))
print_dll(head)


