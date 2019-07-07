class Node:

    def __init__(self, data):
        self.element = data
        self.next_node = None
        self.prev_node = None


class DoubleLinkedList:

    def __init__(self):

        # Initialize blank head and tail node
        self.head_node = None

        # Save linked list size
        self.list_size = 0

    def isEmpty(self):
        return self.list_size is 0

    def pushNode(self, element):

        # Create new node
        new_node = Node(element)
        new_node.next_node = self.head_node

        # Setup head_node's prev_node
        self.head_node.prev_node = new_node

        # Set new_node as head_node
        self.head_node = new_node

        self.list_size += 1

    def removeFrontNode(self):

        # Check if list is empty
        if self.isEmpty():
            print("NodeList is empty")
            return None

        # Check if there are more than 1 nodes
        if self.head_node.next_node:

            # Setup head_node and new one
            curr_head = self.head_node
            next_head = curr_head.next_node

            # Empty curr_head
            curr_head = None

            # Setup new head_node
            self.head_node = next_head

        else:

            # Execute if head_node is the only node
            self.head_node = None

        self.list_size -= 1

    def removeRearNode(self):

        # Check if list is empty
        if self.isEmpty():
            print("NodeList is empty")
            return None

        # Check if head_node is alone because it could also be a tail node
        if self.head_node.next_node is None:
            self.head_node = None

        else:

            # Create current node
            curr_node = self.head_node

            # Go last node
            while curr_node.next_node:
                curr_node = curr_node.next_node

            # Remove link to previous node
            curr_node.prev_node.next_node = None
            curr_node = None


    def addNode(self, element):

        if self.isEmpty():

            # Create new node
            new_node = Node(element)

            # Set new_node as head_node
            self.head_node = new_node

        else:

            # Create a new node
            new_node = Node(element)

            # Set current node
            curr_node = self.head_node

            # Go through link list until the end
            while curr_node.next_node is not None:
                curr_node = curr_node.next_node

            # Set curr_node as previous node of new_node
            curr_node.next_node = new_node
            new_node.prev_node = curr_node

        self.list_size += 1

    def deleteNode(self, element):

        # Check if list is empty
        if self.isEmpty():
            print("NodeList is empty")
            return None

        # Check if head_node has the element
        if self.head_node.element == element:

            # Check if head_node isn't the only node
            if self.head_node.next_node:

                # Get head_node and its next_node
                curr_head = self.head_node
                next_head = curr_head.next_node

                # Create links and delete curr_head
                next_head.prev_node = None
                next_head.next_node = None
                curr_head = None

                # Set new head_node
                self.head_node = next_head

            else:

                # Execute if node is by itself
                self.head_node = None

            return None

        # If node is at rear or other position
        curr_node = self.head_node

        # Continue while node is not empty
        while curr_node:

            if curr_node.element is element:
                # Exchange links
                curr_node.prev_node.next_node = curr_node.next_node
                curr_node.next_node.prev_node = curr_node.prev_node

                # Delete node
                curr_node = None

                # Exit function
                return None

            curr_node = curr_node.next_node

        # Executed ONLY if node doesn't exist
        print("Node w/ {} was not found! ".format(element))

    def printList(self):

        # Set current node
        curr_node = self.head_node

        while curr_node:
            # Print element
            print(curr_node.element)

            # Move to next node
            curr_node = curr_node.next_node


linklist = DoubleLinkedList()
linklist.addNode(1)
linklist.addNode(2)
linklist.addNode(3)

linklist.removeRearNode()
linklist.printList()