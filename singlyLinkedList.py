class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList():
    def __init__(self):
        self.head=None
    def insert_at_beginning(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def insert_at_end(self,data):
        new_node=Node(data) 
        if not self.head:
            self.head=new_node
            return
        current_node=self.head
        while current_node.next:
            current_node=current_node.next
        current_node.next=new_node
            
    def insert_at_position(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        count = 0
        while current_node and count < pos - 1:
            current_node = current_node.next
            count += 1
        if not current_node:
            print("Position out of bounds")
            return
        new_node.next = current_node.next
        current_node.next = new_node

        
        
    def delete_first(self):
        current_node=self.head
        self.head=current_node.next
        del current_node
    def delete_last(self):
        if not self.head:
            print("No eleemnt to be deleted")
            return
        current_node=self.head
        while current_node.next.next:
            current_node=current_node.next
        temp=current_node.next
        current_node.next=None
        del temp
        
    def delete_by_value(self,value):
        if not self.head:
            print("Empty")
            return
        current_node=self.head
        if current_node.data==value:
            self.head=current_node.next
            return
        prev=None
        while current_node and current_node.data!=value:
            prev=current_node
            current_node=current_node.next
        if not current_node:
            print(f"{value} not found")
            return
        prev.next=current_node.next
        del current_node
    
    def search_by_value(self, value):
        if not self.head:
            print("Empty")
            return
        position = 0
        current_node = self.head
        while current_node:
            if current_node.data == value:
                print(f"The value {value} is found at position {position}")
                return
            current_node = current_node.next
            position += 1
        print(f"{value} not found in the list")

    
    def display(self):
        if not self.head:
            print("Empty")
            return
        current_node=self.head
        while current_node:
            print(current_node.data,end=" -->")
            current_node=current_node.next
        print("None")
def main():
    ll=LinkedList()
    while True:
        print("1.Insert At Beginning\n2.Insert At End\n3.Insert At position\n4.Delete First\n5.Delete Last\n6.Delete By Value\n7.Search By Value\n8.Display\n9.Exit")
        user_choice=int(input("Enter the operation: "))
        if user_choice==1:
            data=input("Enter the data to be added: ")
            ll.insert_at_beginning(data)
            print("\n")
        elif user_choice==2:
            data=input("Enter the data to be added: ")
            ll.insert_at_end(data)
            print("\n")
        elif user_choice==3:
            data=input("Enter the data to be added: ")
            position=int(input("Enter the position"))
            ll.insert_at_position(position,data)
            print("\n")
        elif user_choice==4:
            ll.delete_first()
            print("\n")
        elif user_choice==5:
            ll.delete_last()
            print("\n")
        elif user_choice==6:
            value=input("Enter the value to be deleted")
            ll.delete_by_value(value)
            print("\n")
        elif user_choice==7:
            value=input("Enter the element to be searched")
            ll.search_by_value(value)
            print("\n")
        elif user_choice==8:
            ll.display()
            print("\n")
        elif user_choice==9:
            break
        else:
            print("Enter the operations correctly")
            print("\n")
                
if __name__=="__main__":
    main()
            
            
            
        
            
        
        