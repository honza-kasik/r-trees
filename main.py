from tree import *


def main():
    node = Node()
    child1 = Node()
    child1.add_record(Record(Point(40, 80)))
    child1.add_record(Record(Point(120, 160)))
    child2 = Node()
    child2.add_record(Record(Point(100, 40)))
    child2.add_record(Record(Point(160, 120)))
    child3 = Node()
    child3.add_record(Record(Point(170, 200)))
    node.add_child(child1)
    node.add_child(child3)
    child3.add_child(child2)
    tree = Tree(node)
    win = GraphWin('Face', 800, 600)  # give title and dimensions

    tree.draw(win)

    win.getMouse()
    win.close()

main()
