from Node import ListNode
    

def mergeTwoLists(list1, list2):
        
    prev = dummy = ListNode(None)

    while list1 and list2:

        if list1.val > list2.val:
            prev.next = list2
            list2 = list2.next
        else:
            prev.next = list1
            list1 = list1.next

        prev = prev.next

    if list1:
        prev.next = list1
    if list2:
        prev.next = list2

    return dummy.next