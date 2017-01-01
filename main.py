from tree import *


def main():
    node = Node()
    child1 = Node()
    child2 = Node()
    node.add_child(child1)
    node.add_child(child2)
    child1.add_record(Record(Point(1, 2)))
    child1.add_record(Record(Point(3, 4)))
    child2.add_record(Record(Point(2, 1)))
    child2.add_record(Record(Point(4, 3)))
    tree = Tree(node)
    win = GraphWin('Face', 200, 150)  # give title and dimensions

    tree.draw(win)

    win.getMouse()
    win.close()

main()
