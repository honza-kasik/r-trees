import unittest
from tree import *
from graphics import *

class TestNode(unittest.TestCase):

    def test_insert_record(self):
        n = Node()
        n.add_record(Point(10, 20))
        self.assertEqual(1, len(n.get_records()))

    def test_delete_record(self):
        test_value = Point(20, 40)
        retained_value = Point(100, 200)
        n = Node()
        n.add_record(test_value)
        n.add_record(retained_value)
        self.assertEqual(2, len(n.get_records()))
        n.remove_record(test_value)
        self.assertEqual(n.records, [retained_value])
        self.assertEqual(1, len(n.get_records()))

    def test_is_leaf(self):
        root = Node()
        child1 = Node()
        child2 = Node()
        child3 = Node()
        root.add_child(child1)
        root.add_child(child2)
        child2.add_child(child3)
        self.assertFalse(root.is_leaf())
        self.assertTrue(child1.is_leaf())
        self.assertFalse(child2.is_leaf())
        self.assertTrue(child3.is_leaf())

    def test_rectangle_emerge_point_bottom(self):
        base_point1 = Point(0,0)
        base_point2 = Point(10,20)
        emerged_point = Point(30,40)
        rect = RRectangle(base_point1, base_point2)
        rect.emerge_point(emerged_point)
        self.assertEqual(base_point1.getY(), rect.bottom())

    def test_rectangle_emerge_point_right(self):
        base_point1 = Point(0,0)
        base_point2 = Point(10,20)
        emerged_point = Point(30,40)
        rect = RRectangle(base_point1, base_point2)
        rect.emerge_point(emerged_point)
        self.assertEqual(emerged_point.getX(), rect.right())

    def test_rectangle_emerge_point_top(self):
        base_point1 = Point(0,0)
        base_point2 = Point(10,20)
        emerged_point = Point(30,40)
        rect = RRectangle(base_point1, base_point2)
        rect.emerge_point(emerged_point)
        self.assertEqual(emerged_point.getY(), rect.top())

    def test_rectangle_emerge_point_left(self):
        base_point1 = Point(0,0)
        base_point2 = Point(10,20)
        emerged_point = Point(30,40)
        rect = RRectangle(base_point1, base_point2)
        rect.emerge_point(emerged_point)
        self.assertEqual(base_point1.getX(), rect.left())



if __name__ == '__main__':
    unittest.main()
