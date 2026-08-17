class node():
    def __init__(self, data, next):
        self.data = data
        self.next = next
node2 = node(20, None)
node1 = node(10, node2)
print(node1.data, node1.next.data, node2.next)