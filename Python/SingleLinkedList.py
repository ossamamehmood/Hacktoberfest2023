class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkList():
    def __init__(self):
        self.head = None

    def add_at_start(self, data):
        new_node = Node(data)
        temp = self.head
        new_node.next = self.head

        if self.head is not None:
            while (temp.next != self.head):
                temp = temp.next
            temp.next = new_node

        else:
            new_node.next = new_node
            self.head = new_node

    def add_at_position(self, data, position):
        new_node = Node(data)
        #         self.head = new_node
        #         new_node.next = new_node

        if self.head is None:
            self.head = new_node
            new_node.next = self.head
        else:
            temp = self.head
            counter = 1
            while (temp):
                if (position == counter):
                    temp_node = temp.next
                    new_node.next = temp_node
                    temp.next = new_node
                    break
                temp = temp.next
                counter += 1

    def add_at_end(self, data):
        new_node = Node(data)

    def print_circular_linked_list(self):

        temp = self.head
        if self.head is not None:
            while (True):
                print(temp.data)
                temp = temp.next
                if temp == self.head:
                    break
if __name__ == '__main__' :
    ll = CircularLinkList()
    ll.add_at_start(3)
    ll.add_at_start(2)
    ll.add_at_start(1)

    ll.add_at_position(4,0)
    #ll.add_at_start(1)
    ll.print_circular_linked_list()
