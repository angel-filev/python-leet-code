from src.models.list_node import ListNode


class CompareList(object):
    def compare_lists(self, list1: ListNode, list2: ListNode):
        while list1 is not None and list2 is not None:
            if list1.val != list2.val:
                return False
            list1 = list1.next
            list2 = list2.next
        # if one list is shorter than the other, they are not equal
        return list1 is None and list2 is None
