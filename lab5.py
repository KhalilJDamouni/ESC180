import time as t

class Node:
    def __init__(self, data = None, left = None, right = None):
        '''
        Created a class 'Node' with three attributes, set to None by default.
        data is the cargo of the node, left is the left child, also of type Node
        and right is the right child, also of type Node

        (str, Node, Node) --> None

        >>> Node('hi', Node('this'), Node('also')))

        >>> Node(('I', Node('dont'), Node('know')))

        '''
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        '''
        Returns the value of data stored in the Node.

        (Node) --> str

        >>> (Node('This'))
        'This'
        >>> (Node('Also_This'))
        'Also_This'
        '''
        return (str(self.data))

class BinarySearchTree:

    def __init__(self, root = None):
        '''
        Creates a binary tree when provided with a root,
        setting the root to None by default.

        (Node) --> None

        >>> BinarySearchTree() 

        >>> BinarySearchTree(Node('root'))

        '''
        self.root = root
    
    def insert(self, val):
        '''
        Inserts a Node into the currect position of the tree,
        with left children being smaller than the parent,
        and right children being larger than the parent.

        (Node) --> None

        >>> BinarySearchTree().insert(Node('Word'))

        >>> BinarySearchTree().insert(Node('Another'))

        '''
        if(self.root == None):
            self.root = val
            #print('Making the root to be ', self.root)
            #self.root.right = Node(5)
            #self.root.left = Node(1)
        else:
            #print(self)
            #self.insert_helper(self.root,val)
            current_node = self.root
            while(current_node != None):
                #print('looping')
                if(val.data > current_node.data):
                    #print("Going right")
                    if(current_node.right == None):
                        current_node.right = val
                        current_node = current_node.right
                        return
                    else:
                        current_node = current_node.right
                elif(val.data < current_node.data):
                    #print("Going left")
                    if(current_node.left == None):
                        current_node.left = val
                        current_node = current_node.left
                        return
                    else:
                        current_node = current_node.left
                else:
                    return

    '''
    def insert_helper(self,current_node, val):
        #try: 
        #print(self)
        #print(current_node)
        #print(type(current_node))
        if(current_node == None):
            #print('Here')
            #print('The current_node value is', current_node)
            current_node = Node(val)
            #print('The current_node value NOW is', current_node)
        elif(val.data > current_node.data):
            #print('Right')
            if(current_node.right == None):
                current_node.right = val
            else:
                self.insert_helper(current_node.right,val)
            #print('The current_node RIGHT value NOW is', current_node.right)
        elif(val.data < current_node.data):
            #print('Left')
            #print(type(current_node.left))
            if(current_node.left == None):
                current_node.left = val
            else:
                self.insert_helper(current_node.left,val)
            #print('The current_node LEFT value NOW is', current_node.left)
    '''
    def search(self, val):
        '''Finds whether a value is in a tree.

        (str) --> Boolean

        >>> BinarySearchTree(Node('Word')).search('Word')
        True
        >>> BinarySearchTree(Node('Nope')).search('Word')
        False
        '''
        start = t.time()
        current_node = self.root
        while(current_node != None):
            if(current_node.data == val):
                print('Elapsed Time:', t.time() - start, 'Seconds')
                return True
            if(val < current_node.data):
                current_node = current_node.left
            elif(val > current_node.data):
                current_node = current_node.right
        print('Elapsed Time:', t.time() - start, 'Second')
        return False
            

    def __str__(self):
        '''
        Returns the value held in the root Node of the tree

        (None) --> str

        >>> BinarySearchTree(Node('something'))
        something
        >>> BinarySearchTree(Node('another_thing'))
        another_thing
        '''
        return (str(self.root))
    

def constructBST(filename):
    '''
    Creates the vbinary search tree using a given file.

    (str) --> BinarySearchTree

    >>> constructBST('Example.txt')
    1st_value
    >>> constructBST('Example2.txt')
    Another_1st_value
    '''
    start = t.time()
    myFile = open(filename, 'r')
    content = myFile.read()
    content = content.split('\n')
    if('' in content):
        content.remove('') #MIGHT HAVE TO REMOVE THIS, DEPENDING ON IF THE LAST THING IS AN EMPTY ''
    #print(content)
    #print(type(content))

    tree = BinarySearchTree()
    for value in content:
        #print(value)
        tree.insert(Node(value))
    #print('Time to make tree using file', filename,':',t.time() - start)
    return tree

#print(constructBST('Example.txt'))
#print(BinarySearchTree(Node(5)))

#BinarySearchTree().insert(Node('Another'))

'''
tree1 = constructBST('websites.txt')
tree2 = constructBST('websites2.txt')
print(tree1.search('zzzzdreams.com'))
print(tree2.search('zzzzdreams.com'))
print(tree1.search('Thiswebsitesdornstexist.cnn'))
print(tree2.search('Thiswebsitesdornstexist.cnn'))
#tree = BinarySearchTree()
#tree.insert(Node(6))'''
'''
tree = BinarySearchTree()
#print(tree.root)
tree.insert(Node(5))
tree.insert(Node(3))
tree.insert(Node(6))
tree.insert(Node(7))
print(tree.root.left)
print(tree.root.right)
print(tree.search(5))'''

