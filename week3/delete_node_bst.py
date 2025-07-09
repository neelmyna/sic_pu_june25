def delete_node(self):
        data = int(input('Enter data of the node to be delete: '))
        temp1 = self.root
        temp2 = None
        while temp1.data != data:
            temp2 = temp1
            if data < temp1.data:
                temp1 = temp1.left
            else:
                temp1 = temp1.right
        # temp1 now points to node to be deleted and temp2 points to its parent.
        print(f'Node with data {temp1.data} deleted')

        if temp1 is self.root:
            if temp1.left is None and temp1.right is None:
                self.root = None
            if temp1.left is not None and temp1.right is not None:
                temp3 = temp1.right.left
                if temp3 is None:
                    temp1.right.left = temp1.left
                    self.root = temp1.right
                else:
                    while temp3.left is not None:
                        temp3 = temp3.left
                    temp3.left = temp1.left
        else:
            # CODE IT HERE

        # If node to be deleted is a leaf node:
        if temp1.left is None and temp1.right is None:            
            if temp2 is None:
                self.root = None
            elif temp2.left is temp1:
                temp2.left = None
            else:
                temp2.right = None

        # If node to be deleted has 2 children
        elif temp1.left is not None and temp1.right is not None:
            temp3 = temp1.right.left
            if temp3 is None:
                temp1.right.left = temp1.left
            else:
                while temp3.left is not None:
                    temp3 = temp3.left
                temp3.left = temp1.left
            # if root is the node being deleted
            if temp1 is self.root:
                self.root = temp1.right
            elif temp2.left is temp1:
                temp2.left = temp1.right
            else:
                temp2.right = temp1.right

        # when node to be deleted has exactly one child
        else:
            #link = return () if temp1.left temp1.left else temp1.right
            link = temp1.left # assume temp1 has left child
            if temp1.right:
                link = temp1.right
            if temp2.left is temp1:
                temp2.left = link
            else:
                temp2.right = link