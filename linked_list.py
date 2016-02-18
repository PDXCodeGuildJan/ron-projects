"""Create a LinkedList using two classes"""

__author__ = "Ron Shafii"




class Node():

    def __init__(self, value):
        #creates a linkedlist
        self.value = value
        self.next_node = None


    def __str__(self):
        return str(self.value)




class LinkedList():

    def __init__(self):
        #define head of list
        self.head = None    #create an instance of the node class. this becomes the head node.


    def search(self, Node):
        pass


    def add(self, value):
        #add to the end of the list
        current_node = self.head
        new_node = Node(value)

        if current_node == None:
            self.head = new_node

        else:

            #point the head to the new node

            while current_node.next_node != None:
                current_node = current_node.next_node

            current_node.next_node = new_node








    def remove(self, position):
        #ripped from http://stackoverflow.com/questions/28836760/removing-a-node-in-a-linked-list-using-links
        #finds first thing in a list and removes a value
        current_node = self.head
        previous_node = None
        count = 0
        
        while count != position:
            if current_node.next_node == 0 #verify node isn't empty
                print("Invalid Position")
                return None

            previous_node = current_node
            current_node = current_node.next_node
            count +=1

        previous_node_next_node = current_node.next_node
        return current_node




    def __str__(self):
        current_node = self.head
        

         #create a variable to hold the current item



        #create a  list and loop through the different heads of the item
         node_list = []


         #grab the values from the nodes and place them into the list
         node_list.append(current_node.value)








        

        
       


        return 




#linked_list = LinkedList()


#bob = Node("hello")
#sally = Node("name")
#dave = Node("number")


#bob.next_node = sally
#sally.next_node = dave


#print(sally.next_node)


def main():
   link = LinkedList()
   link.add(4)
   link.add(2)
   link.add(86)
   link.add(4)
   link.add(7)
   print("Current list:", link)
   link.remove(4)
   print("List after first 4 is removed:", link)

   link.remove(4)
   print("List after second 4 is removed:", link)

   print("Success! Attempt to remove a third 4 yielded no crashes!")
   link.remove(4)
   
   # Output of above code:
   # -------------------------
   # Current list: 4 2 86 4 7 
   # List after first 4 is removed: 2 86 4 7 
   # List after second 4 is removed: 2 86 7 
   # Attempt to remove a third 4 yielded no crashes




