class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def push(self, n_value):
        n_node = Node(n_value)
        n_node.next = self.head
        self.head = n_node

    def invert(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def mostrar(self):
        temp = self.head
        while(temp):
            print(temp.value, end=" ")
            temp = temp.next

lista = Linked_List()
lista.push(50)
lista.push(40)
lista.push(30)
lista.push(20)
lista.push(10)

print("Lista original: ")
lista.mostrar()
lista.invert()
print("\n")
print("Lista invertida: ")
lista.mostrar()