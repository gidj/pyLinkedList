class List:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, value):
        new_item = ListObject(value, previous=self.tail)
        if self.length is 0:
            self.head = new_item
        else:
            self.tail.next = new_item
        self.tail = new_item
        self.length += 1

    def prepend(self, value):
        new_item = ListObject(value, next=self.head)
        if self.length is 0:
            self.tail = new_item

        self.head = new_item
        self.length += 1

    def peek(self):
        return self.head

    def print_list(self):
        cursor = self.head
        while cursor:
            cursor.print_item()
            cursor = cursor.next

class ListObject:
    def __init__(self, value, previous=None, next=None):
        self.payload = value
        self.previous = previous
        self.next = next

    def print_item(self):
        print self.payload

