class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_end(self, data):
        new_node = Node(data)
        curr = self.head
        if self.head is None:
            self.head = new_node
        while curr:
            curr = curr.next
            curr.next = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):
        curr = self.head
        prev = self.head
        while curr.next:
            prev = curr
            curr = curr.next
            prev.next = None
            return curr.data

    def search(self,data):
        curr = self.head
        while curr.data == data or curr.next:
            if curr.data == data:
                return True
            else:
                curr = curr.next

    def remove_num(self,data):
        curr = self.head
        prev = self.head
        if self.head.data == data:
            self.head = self.head.next
        while curr.next:
            prev = curr
            curr = curr.next
            if curr.data == data:
                prev.next = curr.next
                curr = curr.next


    def clear_all(self):
        head = None


class LinkedListTail:

    def __init__(self):
        self.head = None
        self.tail = None

    def push_head(self,data):
        new_node = Node(data=data)
        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail = self.head

    def push_end(self,data):
        new_node = Node(data)
        self.tail.next = new_node
        self.tail = new_node

    def remove_head(self):
        new_node = self.head
        self.head = self.head.next
        return new_node.data

    def remove_end(self):
        curr = self.head
        prev = self.head
        while curr.next:
            prev = curr
            curr = curr.next
            prev.next = None
            return curr.data

    def clear_all(self):
        head = None
