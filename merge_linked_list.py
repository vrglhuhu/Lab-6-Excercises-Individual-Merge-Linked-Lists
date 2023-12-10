class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(l1, l2):
    dummy = ListNode(-1)
    current = dummy
    
    while l1 is not None and l2 is not None:
        if l1.val <= l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next
    
    if l1 is not None:
        current.next = l1
    if l2 is not None:
        current.next = l2
    
    return dummy.next

# Function to create a linked list from a list of values
def createLinkedList(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for i in range(1, len(arr)):
        current.next = ListNode(arr[i])
        current = current.next
    return head

# Function to print the merged linked list
def printList(node):
    while node is not None:
        print(node.val, end="→" if node.next else "")
        node = node.next
    print()

# Input from the user for the values of the two sorted linked lists
list1_values = list(map(int, input("Please enter space-separated values for the first list: ").split()))
list2_values = list(map(int, input("Please enter space-separated values for the second list: ").split()))

# Create linked lists from user input values
list1 = createLinkedList(list1_values)
list2 = createLinkedList(list2_values)

# Merge the two sorted linked lists
merged_list = mergeTwoLists(list1, list2)

# Display the merged linked list
print("Merged List: ", end="")
printList(merged_list)
