class Node():
    def __init__(self,data):
        self.data=data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head=None
    def insert_at_end(self,data):
        new_node=Node(data)
        if not self.head:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
            current_node.next=new_node
    
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    
    
    def delete_by_value(self,value):
        current_node=self.head
        if not current_node:
            print("Empty")
            return
        if current_node.data==value:
            self.head=current_node.next
            return
        previous_node=None
        while current_node and current_node.data!=value:
            previous_node=current_node
            current_node=current_node.next
        if not current_node:
            print(f"{value} is not found")
            return 
        previous_node.next=current_node.next
        del current_node

    
    def search_by_value(self,value):
        current_node=self.head
        index=0
        while current_node:
            if current_node.data==value:
                print(f"{value} found at the position {index}")
                return True
            current_node=current_node.next
            index+=1
        print({})
            
        
        
    def display(self):
        current_node=self.head
        if not current_node:
            print("Empty")
            return
        while current_node:
            print(current_node.data,end="-->")
            current_node=current_node.next



ll=LinkedList()
ll.insert_at_beginning(10)
ll.search_by_value(10)
ll.display()
ll.delete_by_value(10)
ll.display()


