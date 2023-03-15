import unittest

from src.linked_lists.compare_list import CompareList
from src.linked_lists.sort_list import SortList
from src.models.list_node import ListNode


class TestSolution(unittest.TestCase):
    def test_example_1(self):
        compare_list = CompareList()

        # Test case 1: Empty lists
        self.assertTrue(compare_list.compare_lists(None, None))

        head = ListNode(4, ListNode(2, ListNode(1, ListNode(3))))
        expected_output = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
        self.assertTrue(compare_list.compare_lists(head, expected_output))
    def test_example_2(self):
        head = ListNode(-1, ListNode(5, ListNode(3, ListNode(4, ListNode(0)))))
        expected_output = ListNode(-1, ListNode(0, ListNode(3, ListNode(4, ListNode(5)))))
        sortList = SortList()
        self.assertEqual(sortList.sort(head), expected_output)

    def test_example_3(self):
        head = None
        expected_output = None
        sortList = SortList()
        self.assertEqual(sortList.sort(head), expected_output)


if __name__ == '__main__':
    unittest.main()
