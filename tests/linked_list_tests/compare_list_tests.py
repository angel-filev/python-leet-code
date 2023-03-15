import unittest
from src.models.list_node import ListNode
from src.linked_lists.compare_list import CompareList

class TestCompareList(unittest.TestCase):
    def test_compare_lists(self):
        compare_list = CompareList()

        # Test case 1: Empty lists
        self.assertTrue(compare_list.compare_lists(None, None))

        # Test case 2: Single element lists, equal values
        list1 = ListNode(1)
        list2 = ListNode(1)
        self.assertTrue(compare_list.compare_lists(list1, list2))

        # Test case 3: Single element lists, different values
        list1 = ListNode(1)
        list2 = ListNode(2)
        self.assertFalse(compare_list.compare_lists(list1, list2))

        # Test case 4: Multiple element lists, equal values
        list1 = ListNode(1, ListNode(2, ListNode(3)))
        list2 = ListNode(1, ListNode(2, ListNode(3)))
        self.assertTrue(compare_list.compare_lists(list1, list2))

        # Test case 5: Multiple element lists, different values
        list1 = ListNode(1, ListNode(2, ListNode(3)))
        list2 = ListNode(1, ListNode(2, ListNode(4)))
        self.assertFalse(compare_list.compare_lists(list1, list2))

        # Test case 6: Different length lists
        list1 = ListNode(1, ListNode(2))
        list2 = ListNode(1, ListNode(2, ListNode(3)))
        self.assertFalse(compare_list.compare_lists(list1, list2))

if __name__ == '__main__':
    unittest.main()
