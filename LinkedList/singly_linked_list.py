from LinkedList.base_classes import Node, BaseLinkedList

class SinglyLinkedList(BaseLinkedList):
    def add_nodes(self, elements):
        if elements and self.is_linkedlist_empty():
            item = elements.pop(0)
            node = self.create_node(item)
            self.head = node

        last_node = self._get_last_node()

        for item in elements:
            node = self.create_node(item)
            last_node.set_next(node)
            last_node = last_node.get_next()

    def add_node(self, element):
        node = self.create_node(element)

        if self.is_linkedlist_empty():
            self.head = node
            return
        last_node = self._get_last_node()
        last_node.set_next(node)

    def _get_formatted_list(self, end_point):
        current_node = self.head
        linklist = self.start_sign
        while current_node != end_point:
            linklist += '{0}{1}'.format(current_node.get_data(),self.arrow)
            current_node = current_node.get_next()
        linklist += self.end_sign
        return linklist

    def print_linked_list(self, end_point=None):
        if self.is_linkedlist_empty():
            print('No nodes in list')
            return
        print(self._get_formatted_list(end_point))

    def _get_last_node(self):
        current_node = self.head
        while current_node.get_next():
            current_node = current_node.get_next()
        return current_node