class singly_node():

    def __init__(self, val = 0):
        self.val = val
        self.next = None

    def set_next(self, Node):
        self.next = Node


class doubly_node():

    def __init(self, val = 0):
        self.val = val
        self.next = None
        self.prev = None

    def set_next(self, Node):
        self.next = Node

    def set_prev(self, Node):
        self.prev = Node


