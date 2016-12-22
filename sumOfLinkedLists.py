class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class linked_list:
    def __init__(self):
        self.cur_node = None

    def add_node(self, data):
        new_node = ListNode(data) # create a new node
        new_node.next = self.cur_node # link the new node to the 'previous' node.
        self.cur_node = new_node #  set the current node to the new one.

    def list_print(self):
        node = self.cur_node # cant point to ll!
        while node:
            print node.data
            node = node.next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        l = linked_list()
        carry = 0
        while l1 and l2:
            x = l1.val+l2.val
            if carry > 0:
                x = x + carry
                carry = 0
            if x > 9:
                x = 0
                carry = 1
            l.add_node(x)
            l1 = l1.next
            l2 = l2.next
        return l 