import unittest
from singelist import SingleList, Node


class TestSingleList(unittest.TestCase):
    def setUp(self):
        self.single_list = SingleList()
        for i in range(1, 10):
            self.single_list.insert_tail(Node(i))

    def test_removeTail(self):
        node = Node(9)
        self.assertEqual(self.single_list.remove_tail().data, node.data)

    def test_join(self):
        single_list2 = SingleList()
        for i in range(10, 12):
            single_list2.insert_tail(Node(i))

        self.single_list.join(single_list2)
        node = self.single_list.head

        single_list3 = SingleList()
        for i in range(1, 12):
            single_list3.insert_tail(Node(i))

        node = self.single_list.head
        node2 = single_list3.head
        for i in range(0, self.single_list.length):
            self.assertEqual(node.data, node2.data)
            node = node.next
            node2 = node2.next

    def test_join2(self):
        single_list2 = SingleList()
        single_list2.join(self.single_list)
        node = self.single_list.head
        node2 = single_list2.head
        for i in range(0, self.single_list.length):
            self.assertEqual(node.data, node2.data)
            node = node.next
            node2 = node2.next


if __name__ == '__main__':
    unittest.main()
