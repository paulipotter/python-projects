# A Linked List Item
class Item:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


# Because the assignment requires to "pop" a card from the top of the deck
# and "push" to the back of the deck, I decided to implement a queue using 
# a linked list to track the order of the items in the deck/queue (FIFO)

# Implement data structure Q 
class Q:
    def __init__(self):
        self.back = None
        self.front = None
        self.cnt = 0

    def __repr__(self):
        items = []
        item = self.front
        while item is not None:
            items.append(str(item.data))
            item = item.next
        # items.append("None")
        return "->".join(items)

    def __iter__(self):
        return QIterator(self.front)

    # Returns the ~count~ (aka size) of the Q
    def size(self):
        return self.cnt

    # Returns true if both front and back items are empty
    def is_empty(self):
        return self.back is None and self.front is None

    # "Push" an item at the bottom of the Q
    def push(self, q_item):
        print('Push', q_item)
        # q_item is the item that will be pushed into the bottom of the Q
        # Create an item object
        item = Item(q_item)

        # If Q is not empty, update the back item
        if self.front is not None:
            self.back.next = item
            self.back = item
        else:
            # If Q is empty, initialize both front and back
            self.front = item
            self.back = item

        # Since we "pushed" a new item, increase the count by 1
        self.cnt += 1

    # "Pop" the element at the top of the Q
    def pop(self):

        # If the list is empty, exit with error
        if self.front is None:
            print('Queue Underflow')
            exit(-1)

        # If there's no error, set a variable tmp to the item in front of the linked list
        tmp = self.front
        print('Pop', tmp.data)

        # Move front to the next item in the linked list
        self.front = self.front.next

        # if the list becomes empty
        if self.front is None:
            self.back = None

        # Decrease the count of the q by 1
        self.cnt -= 1

        # Return the popped item
        return tmp.data

    # Returns the top element in the queue
    def top(self):
        # If Q not empty, return the data
        if self.front:
            return self.front.data
        # If Q is empty, throw an error
        else:
            exit(-1)

    # Prints the entire queue contents
    def display(self):
        tmp = []
        for item in self:
            tmp.append(self.item.data)
        print(tmp)


class QIterator:
    def __init__(self, front):
        self.current = front

    def __iter__(self):
        return self

    def __next__(self):
        if not self.current:
            raise StopIteration
        else:
            item = self.current.data()
            self.current = self.current.next.data()
            return item


if __name__ == '__main__':
    q = Q()
    q.push(1)
    q.push(2)
    q.push(3)
    q.push(4)

    print('The front element is', q.top())

    q.pop()
    q.pop()
    q.pop()
    q.pop()

    if q.is_empty():
        print('The queue is empty')
    else:
        print('The queue is not empty')
