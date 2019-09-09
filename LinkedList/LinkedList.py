from LinkedList import Node

class LinkedList:

    def __init__(self, head = None):
        self.head = head

    def insert(self, val):
        new_node = Node(val) # create the node itself
        new_node.set_next(self.head) # point the new node to point to previous node
        self.head = new_node # change the actual head of the linked list to point to the new node itself

    def count(self):
        current = self.head
        count = 0

        while(current.next):
            current = current.get_next()
            count = count + 1

        return count

    def search(self, val_to_find):
        current = self.head

        # proceed to see the rest of the nodes in the LinkedList.
        while (current.next):
            if current.val == val_to_find:
                return current
            current = current.get_next()

        # if goes through the entire list and can't seem to to find the val
        print("Cant find the value in the LinkedList")


    def delete(self, val_to_delete):
        current = self.head
        previous = None

        # Best case scenario where the first one is a match
        if current.val == val_to_delete:
            self.head = current.get_next() # just move the pointer of the LinkedList to the next one.
            return 1

        # In other cases, iterate through the rest of the LinkedList and see what's going on.
        while (current.next):
           previous = current
           current = current.get_next()

           if current.val == val_to_delete:
               previous.set_next(current.get_next())
               return 1

        print("Couldn't find the value to delete after going through the entire list.")








