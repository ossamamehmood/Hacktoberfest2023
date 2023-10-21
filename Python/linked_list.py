
# Create a Node class to create a node
class Node:
    def __init__(self, data = None, next = None, prev = None):
        self.data = data
        self.next = next
        self.prev = prev

# Create a LinkedList class
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self, data):
        if self.head == None :
            node = Node(data, self.head, None)
            self.head = node
        else :
            node = Node(data, self.head, None)
            self.head.prev = node
            self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
        itr = self.head
        liststr = ''
          
        while itr:
            liststr += str(itr.data) + "-->"
            itr = itr.next
        print(liststr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)
            return

        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None)

    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_lenght(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_element(self, index):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invaid Index")
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
            return
          
        count = 0
        itr = self.head
        while itr:
            if count == index :
                itr.prev.next = itr.next
                if itr.next :
                    itr.next.prev = itr.prev
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_lenght():
            raise Exception("Invaid Index")
        if index == 0:
            self.insert_at_begining()
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next, itr)
                if node.next :
                    node.next.prev = node
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:
            return
        if self.head.data == data_after:
            self.head.next = Node(data_to_insert, self.head.next)

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def print_forward(self) :
        if self.head is None:
            return
        itr = self.head
        liststr = ''
        while  itr:
            liststr +=  str(itr.data) + "-"
            itr = itr.next
        print(liststr)

    def get_last_node(self):
        if self.head is None:
            print("List is empty")
            return
        liststr = ''
        itr = self.head
        while itr:
            liststr = str(itr.data)
            itr = itr.next
        print(liststr)

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        liststr = ''
        last_item = self.get_last_node()
        itr = last_item
        while itr:
            liststr += itr.data + "-"
            itr = itr.prev
        print(liststr)

ll = LinkedList()
ll.insert_values(["banana", "mango", "grapes", "orange"])
ll.print()
ll.insert_after_value("mango","apple")
ll.print()
ll.remove_by_value("grapes")
ll.print()
