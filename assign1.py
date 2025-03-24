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

    def search(self,data):
        temp=self.start
        while temp is not None:         #List is not none
            if temp.item==data:
                return temp
            temp=temp.next

        return None
    
    def insert_after(self,temp,data):
        if temp is not None:
            n=Node(data,temp.next)
            temp.next=n


#driver code
mylist=SLL()