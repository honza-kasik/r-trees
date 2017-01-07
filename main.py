from tree import *


def main():
    node = Node()
    child1 = Node()
    child2 = Node()
    node.add_child(child1)
    node.add_child(child2)
    child1.add_record(Record(Point(10, 20)))
    child1.add_record(Record(Point(30, 40)))
    child2.add_record(Record(Point(20, 10)))
    child2.add_record(Record(Point(40, 30)))
    tree = Tree(node)
    win = GraphWin('Face', 200, 150)  # give title and dimensions

    tree.draw(win)

    win.getMouse()
    win.close()

main()
