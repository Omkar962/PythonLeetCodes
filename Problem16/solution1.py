# Time Complexity :- O(n) where n is the number of nodes in the linked list (since we traverse the list once).
# Space Complexity :- O(1) as we modify the linked list in place without using extra memory.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    current = head
    
    while current and current.next:
        if current.val == current.next.val:
            current.next = current.next.next  # Skip duplicate node
        else:
            current = current.next  # Move to next distinct node
    
    return head
