from single_linked_list import SingleLinkedList


def test_single_linked_list():
    lst = SingleLinkedList()
    lst.print_list()
    lst.append_to_tail(1)
    lst.append_to_tail(2)
    lst.append_to_tail(3)
    lst.print_list()
    lst.append_to_tail(4)
    lst.append_to_tail(5)
    lst.print_list()
    lst.delete_node(1)
    lst.print_list()

    lst.delete_node(3)
    lst.print_list()

    lst.delete_node(5)
    lst.print_list()
