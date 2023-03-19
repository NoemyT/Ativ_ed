class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Linked_List:
    def __init__(self):
        self.head = None

    def swap(self, x, y):
        if x == y: return
        prevx = None
        currx = self.head
        while(currx != None and currx.value != x):
            prevx = currx
            currx = currx.next
        prevy = None
        curry = self.head
        while(curry != None and curry.value != y):
            prevy = curry
            curry = curry.next
        if currx == None or curry == None: return
        if prevx != None:
            prevx.next = curry
        else:
            self.head = curry
        if prevy != None:
            prevy.next = currx
        else:
            self.head = currx
        temp = currx.next
        currx.next = curry.next
        curry.next = temp

    def BubbleSort(self):
        count = 0
        start = self.head
        while(start != None):
            count += 1
            start = start.next
        for i in range(0, count):
            start = self.head
            while(start != None):
                ptr = start.next
                if ptr != None:
                    if start.value > ptr.value:
                        self.swap(start.value, ptr.value)
                start = start.next

    def mostrar(self):
        tmp = self.head
        while(tmp != None):
            print(tmp.value, end = " ")
            tmp = tmp.next

if __name__ == '__main__':
    arr = [95, 34, 56, 74, 12, 65, 87]

    lista = Linked_List()
    lista.head = Node(arr[0])
    start = lista.head
    for i in range(1, len(arr)):
        start.next = Node(arr[i])
        start = start.next

    print("Lista original:")
    lista.mostrar()
    lista.BubbleSort()
    print("\n")
    print("Lista ordenada:")
    lista.mostrar()    