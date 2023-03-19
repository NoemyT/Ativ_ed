class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_list:
    def __init__(self):
        self.head = None

    def Inst_sort(self, n_node):
        if self.head is None:
            n_node.next = self.head
            self.head = n_node
        elif self.head.value >= n_node.value:
            n_node.next = self.head
            self.head = n_node
        else:
            current = self.head
            while(current.next is not None and current.next.value < n_node.value):
                current = current.next

            n_node.next = current.next
            current.next = n_node

    def push(self, n_value):
        n_node = Node(n_value)
        n_node.next = self.head
        self.head = n_node

    def mostrar(self):
        temp = self.head
        while(temp):
            print (temp.value)
            temp = temp.next

lista = Linked_list()
n_node = Node(8)
lista.Inst_sort(n_node)
n_node = Node(16)
lista.Inst_sort(n_node)
n_node = Node(32)
lista.Inst_sort(n_node)
n_node = Node(40)
lista.Inst_sort(n_node)
n_node = Node(24)
lista.Inst_sort(n_node)
n_node = Node(48)
lista.Inst_sort(n_node)
n_node = Node(56)
lista.Inst_sort(n_node)
n_node = Node(72)
lista.Inst_sort(n_node)
n_node = Node(80)
lista.Inst_sort(n_node)
n_node = Node(64)
lista.Inst_sort(n_node)
print("Tabuada do 8 [1-10]:")
lista.mostrar()