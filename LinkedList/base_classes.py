class Node(object):
    """
    Node
        Will contain the info for a node of link list
        which contains an element and an address of next node
    """
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node

    def has_next(self):
        return self.next != None

    def has_data(self):
        return self.data != None


class BaseLinkedList(object):
    start_sign = '!->'
    end_sign = "#\n"
    arrow = '->'

    def __init__(self):
        self.head = None

    def is_linkedlist_empty(self):
        return self.head == None

    def create_node(self, item):
        return Node(item)