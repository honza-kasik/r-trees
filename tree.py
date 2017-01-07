from graphics import *
import math


class VisualRepresentation:

    def __init__(self, r):
        if not (isinstance(r, Rectangle) or isinstance(r, Point)):
            print("Invalid visual representation type!")
        else:
            self.r = r

    def bottom(self):
        r = self.r
        if isinstance(r, Rectangle):
            if r.getP1().getY() > r.getP2().getY():
                return r.getP2().getY()
            else:
                return r.getP1().getY()
        else:
            return r.getY()

    def top(self):
        r = self.r
        if isinstance(r, Rectangle):
            if r.getP1().getY() > r.getP2().getY():
                return r.getP1().getY()
            else:
                return r.getP2().getY()
        else:
            return r.getY()

    def right(self):
        r = self.r
        if isinstance(r, Rectangle):
            if r.getP1().getX() > r.getP2().getX():
                return r.getP1().getX()
            else:
                return r.getP2().getX()
        else:
            return r.getX()

    def left(self):
        r = self.r
        if isinstance(r, Rectangle):
            if r.getP1().getX() > r.getP2().getX():
                return r.getP2().getX()
            else:
                return r.getP1().getX()
        else:
            return r.getX()

    def area(self):
        return (self.right() - self.left()) * (self.top() - self.bottom())

    def emerge_point(self, point: Point):
        max_left = self.left()
        max_right = self.right()
        max_top = self.top()
        max_bottom = self.bottom()
        if point.getY() > max_top:
            max_top = point.getY()
        if point.getY() < max_bottom:
            max_bottom = point.getY()
        if point.getX() > max_right:
            max_right = point.getX()
        if point.getX() < max_left:
            max_left = point.getX()
        return VisualRepresentation(Rectangle(Point(max_left, max_bottom), Point(max_right, max_top)))

    def draw(self, win):
        self.r.draw(win)


class VisuallyRepresentedItem:
    def visual_representation(self) -> VisualRepresentation:
        print("This method was not overloaded!")


class Record(VisuallyRepresentedItem):

    def __init__(self, value: Point):
        self.value = value
        self._visual_representation = VisualRepresentation(value)

    def visual_representation(self) -> VisualRepresentation:
        return self._visual_representation


class Node(VisuallyRepresentedItem):
    def __init__(self):
        self.records = []
        self.children = []
        self.vr = None

    def count_of_records(self):
        return len(self.records)

    def add_record(self, record: Record):
        self.records.append(record)
        self.update_visual_representation()

    def get_children(self):
        return self.children

    def add_child(self, child):
        self.children.append(child)
        self.update_visual_representation()

    def remove_record(self, record: Record):
        self.records.remove(record)

    def is_leaf(self):
        return len(self.children) == 0

    def visual_representation(self) -> VisualRepresentation:
        if self.vr is None:
            self.update_visual_representation()
        return self.vr

    def update_visual_representation(self):
        left_max = math.inf
        top_max = -math.inf
        right_max = -math.inf
        bottom_max = math.inf

        examined_set = self.children
        if self.is_leaf():
            examined_set = self.records

        for item in examined_set:
            print(str(item))
            r = item.visual_representation()
            if r.left() < left_max:
                left_max = r.left()
            if r.right() > right_max:
                right_max = r.right()
            if r.top() > top_max:
                top_max = r.top()
            if r.bottom() < bottom_max:
                bottom_max = r.bottom()
        # return enclosing rectangle
        self.vr = VisualRepresentation(Rectangle(Point(left_max, bottom_max),
                                                 Point(right_max, top_max)))


class Tree:
    min_cap = 2
    max_cap = min_cap * 2

    def __init__(self, root: Node):
        self.root = root

    def __pick_subtree(self, n: Node, point: Point) -> Node:
        smallest_expansion = math.inf
        picked_node = None
        for child in n.children:
            child_vr = child.visual_representation()
            tmp_vr = child_vr.emerge_point(point)
            expansion = child_vr.area() - tmp_vr.area()
            if expansion < smallest_expansion or (  # expansion is same as smallest expansion, compare rectangle areas
                    expansion == smallest_expansion and child_vr.area() < picked_node.visual_representation().area()):
                smallest_expansion = expansion
                picked_node = child
        return picked_node

    # Choose leaf to which new index record will be placed
    def _choose_leaf(self, point: Point):
        n = self.root
        while not n.is_leaf():
            n = self.__pick_subtree(n, point)
        return n

    def _adjust_tree(self):
        pass

    def _split_node(self):
        pass

    def insert(self, x, y):
        point = Point(x, y)
        picked_node = self._choose_leaf(point)
        if picked_node.count_of_records() < self.max_cap:
            picked_node.add_record(Record(point))
        else:
            pass
            # split node etc...

    def draw(self, win):
        n = self.root
        n.visual_representation().draw(win)
        for child in n.children:
            child.visual_representation().draw(win)
            if child.is_leaf():
                for record in child.records:
                    record.visual_representation().draw(win)
