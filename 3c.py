#! /usr/bin/python

'''
Node
    __init__(self, node_name = None, node_next = None)
Linked_list
    __init__(self)
    __str__(self)
    insert(self, node_name)
    size(self)
    search(self, node_name)
'''

# Linked list
# Doubly linked list?????

class Node(object):
    def __init__(self, node_name = None, node_next = None):
        self.node_name = node_name
        self.node_next = node_next

class Linked_List(object):

    def __init__(self):
        self.size = 0
        self.head = None

    def __str__(self):
        statement = []
        if not self.size:
            return str(tuple(statement))
        temp = self.head
        while temp:
            statement.append(temp.node_name)
            temp = temp.node_next
        return(str(tuple(statement)))

    def apnd(self, node_name):
        if not self.head:
            self.head = Node(node_name)
        else:
            self.head = Node(node_name, self.head)
        self.size += 1

    def insert(self, node_name, prev_node):
        self.search(node_name)

    def size(self):
        return self.size

    def search(self, node_name):
        try:
            temp = self.head
            while True:
                if temp.node_name == node_name:
                    result = temp
                    break
                else:
                    if not temp.node_next:
                        result = None
                        break
                    else:
                        temp = temp.node_next
            return result
        except AttributeError:
            return None

    def listify(self):
        temp = self.head
        l = []
        while temp:
            l.append(temp.node_name)
            temp = temp.node_next
        l.reverse()
        l = "".join(l)
        return l

def answer(words):
    lis = Linked_List()
    for w in words:
        if not lis.search(w[0]):
            lis.apnd(w[0])
    print(lis)
    li = lis.listify()
    return li

print(answer(['word', 'words', 'something','another','new','newnew']))
