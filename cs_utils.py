## Utilities for code signals problems sets.  What I need is a way to test with a raw list input
## 
def list_string_to_list(inputStr):
    return eval(inputStr)

class lListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def list_string_to_linked_list(inputStr):
    l = None
    curr = None
    for val in list_string_to_list(inputStr):
        node = lListNode(val)
        if curr is not None:
            curr.next = node
            curr = node
        else:
            l = node
            curr = node

    return l


## we will also need to express output as lists printed as strings
def list_to_string(li):
    return str(li)

def iterate_ll(ll):
    curr = ll
    while curr is not None:
        yield curr.value
        curr = curr.next

def ll_to_string(ll):
    return list_to_string(list(iterate_ll(ll)))


## Debuging and testing

if __name__ == "__main__":
    # Test Sting to list funcs
    list_string = "[0, 1, 1, 2, 3, 5, 8]"
    print("List_to_string Tested with '[0, 1, 1, 2, 3, 5, 8]'")
    print(list_to_string(list_string_to_list(list_string)))

    # Test Sting to linked List funcs
    list_string = "[0, 1, 1, 2, 3, 5, 8, 13]"
    print("Linked_List_to_string Tested with '[0, 1, 1, 2, 3, 5, 8, 13]'")
    print(ll_to_string(list_string_to_linked_list(list_string)))
