class No:
    def __init__(self, x):
        self.val = x
        self.next = None

def delete_node(no_atual, value):   
    while no_atual.next != None:        
        if no_atual.val == value:
            no_anterior.next = no_atual.next
            # delete(no_atual)
            return None
       
        # print(no_atual.val)
        no_anterior = no_atual
        no_atual = no_atual.next


node1 = No(5)
head = node1
node2 = No(8)
node1.next = node2
node3 = No(9)
node2.next = node3

print(head.val)
print(node1.next.val)
delete_node(head, 8)
print(node1.next.val)
print(head.val)

#The given node will not be the tail and it will always be a valid node of the linked list.

# proximo = head.next
# print(proximo)
# print(node2)