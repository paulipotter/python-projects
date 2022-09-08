class Item:
    """
    A class to represent a single item in the linked list
    """

    def __init__(self, data):
        """
        Constructs all the attributes for the item object
        :param data: the data to be stored in the relevant item
        """
        self.data = data
        self.next = None

    def __repr__(self):
        """
        Returns the string representation of itself
        :return: self.data as a str
        """
        return self.data


class Q:
    """
    A class to implement the Custom Queue Q

    Because the assignment requires to "pop" a card from the
    top of the deck and "push" to the back of the deck,
    I decided to implement a queue using a linked list
    to track the order of the items in the deck/queue (FIFO).
    """

    def __init__(self):
        """
        Constructs all the attributes for the item object
        """
        self.back = None
        self.front = None
        self.cnt = 0

    def __repr__(self):
        """
        Returns the string representation of itself
        :return: a string representation of the current
                 state of the Q, with indicators showing
                 the front and the back of it.
        """
        items = []
        item = self.front
        while item is not None:
            items.append(str(item.data))
            item = item.next

        representation = "[front]" + "->".join(items) + "[back]"
        return representation

    def size(self):
        """
        Returns the ~count~ (aka size) of the Q
        :return: the count/size of the Q
        """
        return self.cnt

    def is_empty(self):
        """
        Returns true if the Q is empty
        :return:
        """
        return self.back is None and self.front is None

    def push(self, q_item):
        """
        "Pushes" an item at the bottom of the Q
        :param q_item: variable that will be initialized
                       as an Item() and pushed into the
                       bottom of the Q
        """

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

    def pop(self):
        """
        "Pops" the element at the top of the Q
            aka: returns the item at the top
            of the Q and removes the item from the Q
        :return: the popped element
        """

        # If the list is empty, exit with error
        if self.front is None:
            print('Queue Underflow')
            exit(-1)

        # If there's no error, set a variable tmp to the item in front of the linked list
        tmp = self.front

        # Move front to the next item in the linked list
        self.front = self.front.next

        # if the list becomes empty
        if self.front is None:
            self.back = None

        # Decrease the count of the q by 1
        self.cnt -= 1

        # Return the popped item
        return tmp.data
