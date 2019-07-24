class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

    def getPosition(self, position):        
        counter = 1
        if position < 1:
            return None
        current = self.head
        while current and counter <= position:
            if counter == position:
                return current
            counter += 1
            current = current.next
        return None

    def insertAt(self, new_element, position):
        previous = self.getPosition(position - 1)
        if position > 1:
            new_element.next = previous.next.next
            previous.next = new_element
        elif position == 1:
            new_element = self.head
    
    def delete(self, value):
        current = self.head
        previous = None
        while current.next and current.value != value:
            previous = current
            current = current.next
            if current.value == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next

                    
# Test the LinkedList implementation
el1 = Element('A')
el2 = Element(10)
el3 = Element(20)
el4 = Element("Hello")
el5 = Element("World")

ll = LinkedList(el1)
ll.append(el2)
ll.append(el3)

# Should print 20
print(ll.head.next.next.value)

# Get position: should print 20
print(ll.getPosition(3).value)

ll.insertAt(el4, 3)
print(ll.getPosition(3).value) # Should print "Hello"
print(ll.getPosition(2).value) # Should print 10

ll.delete(10)
print(ll.getPosition(2).value) # Should print "Hello"
