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
        return self.list_size == 0

    def pushNode(self, element):

        # Create new node
        new_node = Node(element)
        new_node.next_node = self.head_node

        # Setup head_node's prev_node
        self.head_node.prev_node = new_node

        # Set new_node as head_node
        self.head_node = new_node

        self.list_size += 1

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

        if self.isEmpty():
            print("NodeList is empty")

        else:

            # Set current node
            curr_node = self.head_node

            # Go through link list
            while curr_node.next_node is not None:

                # Break if element matches node's
                if curr_node.element == element:
                    break

                # Move to next node
                curr_node = curr_node.next_node

            # Check if next_node isn't empty
            if curr_node.next_node is not None:
                curr_node.prev_node.next_node = curr_node.next_node
                curr_node.next_node.prev_node = curr_node.prev_node

            # Check if curr_node matches with element
            elif curr_node.element == element:
                curr_node.prev_node.next_node = None

            # Execute only if node isn't found
            else:
                print("Node was not found!")

                # Return nothing to exit function
                return

            # Delete node
            print("Node Deleted: {}".format(curr_node.element))
            del curr_node

            self.list_size -= 1

    def printList(self):

        # Set current node
        curr_node = self.head_node

        while curr_node:

            # Print element
            print(curr_node.element)

            # Move to next node
            curr_node = curr_node.next_node


linkList = DoubleLinkedList()
linkList.addNode(1)
linkList.addNode(11)
linkList.addNode(111)
linkList.addNode(1111)
linkList.pushNode(0)
print(linkList.isEmpty())

#linkList.deleteNode(1)

linkList.printList()
