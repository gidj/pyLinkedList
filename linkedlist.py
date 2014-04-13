class LinkedList:
    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def append(self, value):
        new_item = LinkedListItem(value, previous=self.tail)
        if self.length is 0:
            self.head = new_item
        else:
            self.tail.next = new_item
        self.tail = new_item
        self.length += 1

    def prepend(self, value):
        new_item = LinkedListItem(value, next=self.head)
        if self.length is 0:
            self.tail = new_item

        self.head = new_item
        self.length += 1

    def peek(self):
        return self.head.payload

    def pop(self):
        if self.head:
            value = self.head.payload 
            self._remove(self.head)
            return value
        else:
            return None

    def _remove(self, item):
        # Make sure the item exists; if not, do nothing
        if item:
            # Only access item previous if it exists. If it doesn't exist, item
            # is the head of the list and head needs to be updated
            if item.previous:
                item.previous.next = item.next
            else:
                self.head = item.next

            # Only access item.next if it exists. If it doesn't exist, item is
            # the tail, and tail needs to be updated
            if item.next:
                item.next.previous = item.previous
            else: 
                self.tail = item.previous

            self.length -= 1
        else:
            pass

    def print_list(self):
        cursor = self.head
        while cursor:
            cursor.print_item()
            cursor = cursor.next

    def as_python_list(self):
        """ Return a Python list that is comprised of the values in the Linked
        List from head to tail """
        value = []
        cursor = self.head
        while cursor:
            value.append(cursor.payload)
            cursor = cursor.next
        return value

    def value_by_index(self, index):
        cursor = self.head
        i = 0
        while cursor and i < index:
            cursor = cursor.next
            i += 1

        return cursor.payload

class LinkedListItem:
    def __init__(self, value, previous=None, next=None):
        self.payload = value
        self.previous = previous
        self.next = next

    def print_item(self):
        print self.payload

