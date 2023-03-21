import unittest

from src.queues.priority_queue import PriorityQueue

class TestPriorityQueue(unittest.TestCase):
    def test_push_and_pop(self):
        pq = PriorityQueue()
        pq.push('A', 3)
        pq.push('B', 2)
        pq.push('C', 1)
        self.assertEqual(pq.pop(), 'A')
        self.assertEqual(pq.pop(), 'B')
        self.assertEqual(pq.pop(), 'C')
        self.assertTrue(pq.is_empty())

    def test_is_empty(self):
        pq = PriorityQueue()
        self.assertTrue(pq.is_empty())
        pq.push('A', 1)
        self.assertFalse(pq.is_empty())
        pq.pop()
        self.assertTrue(pq.is_empty())

if __name__ == '__main__':
    unittest.main()
