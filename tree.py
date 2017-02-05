from graphics import *
import math


class Rectangle(Rectangle):
    def __init__(self, p1, p2):
        super().__init__(p1, p2)

    def bottom(self):
        return min(self.getP1().getY(), self.getP2().getY())

    def top(self):
        return max(self.getP1().getY(), self.getP2().getY())

    def right(self):
        return max(self.getP1().getX(), self.getP2().getX())

    def left(self):
        return min(self.getP1().getX(), self.getP2().getX())

    def area(self):
        return (self.right() - self.left()) * (self.top() - self.bottom())

    def emerge_point(self, point: Point):
        max_left = min(self.left(), point.getX())
        max_right = max(self.right(), point.getX())
        max_top = max(self.top(), point.getY())
        max_bottom = min(self.top(), point.getY())
        return self.__init__(Point(max_left, max_top), Point(max_right, max_bottom))

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Rectangle; p1: {0}, p2: {1}>".format(self.p1, self.p2)


class Node:
    def __init__(self):
        self.parent = None
        self.rectangle = None
        self.children = []
        self.records = []

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)

    def is_leaf(self):
        return len(self.children) == 0

    def draw(self, win: GraphWin, level: int):
        self.rectangle.draw(win)
        # todo draw children and values and change color based on level

    def add_record(self, record: Point):
        self.records.append(record)

    def get_records(self):
        return self.records

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return "<Node; Records: {0}, Children: {1}>".format(self.records, self.children)


class Tree:
    min_cap = 2
    max_cap = min_cap * 2

    def __init__(self, root: Node):
        self.root = root

    def __pick_subtree(self, n: Node, point: Point) -> Node:
        smallest_expansion = math.inf
        picked_node = None

        for child in n.get_children():
            tmp_rect = child.rectangle.emerge_point(point)
            expansion = child.rectangle.area() - tmp_rect.area()
            if expansion < smallest_expansion or (  # expansion is same as smallest expansion, compare rectangle areas
                            expansion == smallest_expansion and child.rectangle.area() < picked_node.rectangle.area()):
                smallest_expansion = expansion
                picked_node = child

        return picked_node

    # Choose leaf to which new index record will be placed
    def _choose_leaf(self, point: Point):
        n = self.root
        while not n.is_leaf():
            n = self.__pick_subtree(n, point)
        return n

    def _adjust_tree(self, node: Node):
        pass
        # todo

    def _split_node(self, node: Node):
        return Node(), Node()
        pass
        # todo

    def insert(self, x, y):
        point = Point(x, y)
        chosen_leaf = self._choose_leaf(point)
        chosen_leaf.add_record(point)
        if len(chosen_leaf.get_records()) >= self.max_cap:
            l, ll = self._split_node(chosen_leaf)
            self._adjust_tree(l)
            self._adjust_tree(ll)

    def draw(self, win: GraphWin):
        self.root.draw(win, 0)
