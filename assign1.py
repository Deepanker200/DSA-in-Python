'''Singly Linked List'''


class Node:
    def __init_(self,item=None,next=None):
        self.item=item         #Instance object variables
        self.next=next

        
class SLL:
    def __init__(self,start=None):
        self.start=start

    def is_empty(self):
        return self.start==None

    def insert_at_start(self,data):
        n=Node(data,self.start)
        self.start=n

    def insert_at_last(self,data):
        n=Node(data)        #By default next is none because previously it was at last
        if not self.is_empty():
            temp=self.start
            while temp.next is not None:
                temp=temp.next
            temp.next=n
        else:
            self.start=n

#driver code
mylist=SLL()