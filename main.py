# Define the Node class for a singly linked list
class Node:
    def __init__(self, data):
        """
        Node class for a singly linked list.
        Parameters:
        - data: The data to be stored in the node.
        """
        self.data = data
        self.next = None
# Define the SinglyLinkedList class
class SinglyLinkedList:
    def __init__(self):
        """
        SinglyLinkedList class to manage the linked list operations.
        """
        self.head = None

    def add_node(self, data):
        """
        Add a node to the end of the linked list.
        Time complexity: O(n), where n is the number of nodes in the linked list.
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            
    def display_nodes(self):
        """
        Display all nodes in the linked list.
        Time complexity: O(n), where n is the number of nodes in the linked list.
        """
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

    def search_and_delete(self, value):
        """
        Search for a value in the linked list and delete all nodes with that value.
        """
        current = self.head
        previous = None

        while current:
            if current.data == value:
                if previous:
                    previous.next = current.next
                else:
                    self.head = current.next
                current = None
                return
            else:
                previous = current
                current = current.next
                
def main():
    errors = 0

    while True:
        print("\nWelcome to the program!")
        name = input("Enter your name: ")
        print(f"Hello, {name}!")

        print("\nChoose an option:")
        print("1. Singly Linked List")
        print("2. Check if Palindrome")
        print("3. Priority Queue")
        print("4. Evaluate an Infix Expression")
        print("5. Graph")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            linked_list = SinglyLinkedList()
            while True:
                print("\nSingly Linked List Menu:")
                print("a. Add Node")
                print("b. Display Nodes")
                print("c. Search for & Delete Node")
                print("d. Return to main menu")

                sub_choice = input("Enter your choice: ")

                if sub_choice == 'a':
                    value = int(input("Enter a numerical value: "))
                    linked_list.add_node(value)
                elif sub_choice == 'b':
                    linked_list.display_nodes()
                elif sub_choice == 'c':
                    value = int(input("Enter a value to search and delete: "))
                    linked_list.search_and_delete(value)
                elif sub_choice == 'd':
                    break
                else:
                    print("Invalid choice! Please try again.")

        elif choice == '6':
            print("Goodbye!")
            break

        else:
            print("Error: Invalid choice! Please try again.")
            errors += 1

            if errors >= 4:
                print("Too many consecutive errors. Exiting.")
                break


if __name__ == "__main__":
    main()