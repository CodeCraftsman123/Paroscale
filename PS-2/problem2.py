#Start of the linked list-> Most Recently Used Data
#End of the linked list->Least Recently Used Data

LRU_LIMIT = 2
my_dict = {}
class Node:
    def __init__(self,key,val):
        self.key=key
        self.val = val
        self.prev = None
        self.next = None

class LRU:
    head = Node(-1,-1)
    tail = Node(-1,-1)

    @staticmethod
    def __put_after_head(new_node):
        new_node.next = LRU.head.next
        LRU.head.next = new_node
        new_node.prev = LRU.head
        new_node.next.prev = new_node

    @staticmethod
    def __del_node(old_node):
        old_next = old_node.next
        old_prev = old_node.prev
        old_prev.next = old_next
        old_next.prev = old_prev

        

    @staticmethod
    def put(key,val):
        if key in my_dict:
            old_node = my_dict[key]
            my_dict.pop(key)
            LRU.__del_node(old_node)
            

        if len(my_dict) == LRU_LIMIT:
            my_dict.pop(LRU.tail.prev.key)
            LRU.__del_node(LRU.tail.prev)

        new_node = Node(key,val)
        LRU.__put_after_head(new_node)
        my_dict[key] = new_node

    @staticmethod
    def get(key):
        if key in my_dict:
            ans_node = my_dict[key]
            ans = ans_node.val

            my_dict.pop(key)
            LRU.__del_node(ans_node)

            LRU.__put_after_head(ans_node)
            my_dict[key] = ans_node
            return ans
        else:
            return -1
        
    @staticmethod
    def print_cache():
        print(f"Most Recently used to Least Recently used",end = ":")
        node=LRU.head.next
        while(node.val!=-1):
            print(f"({node.key},{node.val})", end = " ")
            node = node.next
        

                
        
if __name__ == "__main__":
    LRU.head.next = LRU.tail
    LRU.tail.prev = LRU.head

    LRU.print_cache()#Prints nothing, as the cache is empty
    print("\n")

    LRU.put(1,1)
    LRU.print_cache()
    print("\n")

    LRU.put(2,2)
    LRU.print_cache()
    print("\n")

    print(f"Performing get with key 1.Value with key 1:{LRU.get(1)}")
    LRU.print_cache()
    print("\n")
    
    print(f"Performing get with key 3.Value with key 3:{LRU.get(3)}")
    LRU.print_cache()
    print("\n")

    LRU.put(3,3)
    LRU.print_cache()
    print("\n")

    LRU.put(1,3)
    LRU.print_cache()
    print("\n")

    print(f"Performing get with key 3.Value with key 3:{LRU.get(3)}")
    LRU.print_cache()
    print("\n")
