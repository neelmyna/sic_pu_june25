'''
add node
search node
list tree (inorder / preorder / postorder)
delete node
'''

class Node:
    def __init__(self, data = 0):
        if data == 0:
            data = int(input('Enter data of the node: '))
        self.left = None
        self.data = data
        self.right = None

class BST:
    def __init__(self):
        self.root = None
        print('An empty BST is created')

    def add_node(self):
        new_node = Node() # create a new Node object
        if self.root == None: # check if the tree is empty
            self.root = new_node
            return
        temp1 = self.root
        temp2 = None
        while temp1 != None:
            temp2 = temp1
            if new_node.data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        if new_node.data < temp2.data:
            temp2.left = new_node
        else:
            temp2.right = new_node

    def in_order(self, temp):
        if temp == None:
            #print('Tree is empty')
            return
        self.in_order(temp.left)
        print(temp.data, end = '  ')
        self.in_order(temp.right)
    
    def pre_order(self, temp):
        if temp != None:
            print(temp.data, end = '  ')
            self.pre_order(temp.left)
            self.pre_order(temp.right)

    def post_order(self, temp):
        if temp == None:
            return
        self.post_order(temp.left)
        self.post_order(temp.right)
        print(temp.data, end = '  ')

    def search_node(self, temp, search_data):
        found = False
        if temp != None:
            if temp.data == search_data:
                return True
            found = self.search_node(temp.left, search_data)
            if found:
                return found
            found = self.search_node(temp.right, search_data)
        return found
    
    def delete_node(self, temp, delete_data):
        if temp == None:
            return
    

class Menu:
    def __init__(self):
        self.choice = 0

    def is_tree_empty(self, bst):
        if bst.root == None:
            print('Tree is empty')
            return True
        return False

    def menu(self, bst):
        match self.choice:
            case 1 : bst.add_node()
            case 2 :
                if self.is_tree_empty(bst):
                    return
                search_data = int(input('Enter data of the node to be serached: '))
                found = bst.search_node(bst.root, search_data)
                if found:
                    print(f'Node with data {search_data} found')
                else:
                    print(f'Node with data {search_data} not found')
            case 3 : 
                if self.is_tree_empty(bst):
                    return
                bst.in_order(bst.root)
            case 4 : 
                if self.is_tree_empty(bst):
                    return
                bst.pre_order(bst.root)
            case 5 : 
                if self.is_tree_empty(bst):
                    return
                bst.post_order(bst.root)
            case 6 : 
                if self.is_tree_empty(bst):
                    return
                delete_data = int(input('Enter data of the node to be deleted: '))
                bst.delete_node(bst.root, delete_data)
            case 7 : self.choice = 0
            case _ : print('Invalid choice')

    
    def start_app(self):
        bst = BST()
        while True:
            print('1:Add 2:Search 3:Inorder 4:PreOrder 5:PostOrder 6:Delete 7:Exit')
            self.choice = int(input('Enter your choice: '))
            self.menu(bst)
            if self.choice == 0:
                print('Application closed')
                break
                
menu = Menu()
menu.start_app()

