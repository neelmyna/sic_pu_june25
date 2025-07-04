class Student:
    def __init__(self, id = 0, name = '', marks = 0.0):
        self.id = id
        self.name = name
        self.marks = marks

    def __str__(self):
        print(f'ID= {self.id}, Name={self.name}, Marks={self.marks}')

class Node:
    def __init__(self, student = None):
        self.data = student
        self.link = None
    
    def create_student(self):
        id = int(input('Enter Id of the student: '))
        name = (input('Enter Name of the student: '))
        marks = float((input('Enter Marks of the student: ')))
        student = Student(id, name, marks)
        return student

class Queue:
    def __init__(self):
        self.front = None

    def insert(self):
        node = Node() # craete Node object
        student = node.create_student() # create student object 
        node.data = student # set the student object as data of the node
        if self.front == None:
            self.front = node
            return
        node.link = self.front
        self.front = node

    def delete(self):
        if self.front == None:
            print('Queue is empty')
            return
        if self.front.link == None:
            print(f'Deleted Node data is: {self.front.data}')
            self.front = None
            return

        temp = self.front # Copy address of 1st node
        while temp.link.link != None: # untill last but node is reached
            temp = temp.link # traverse to next node
        print(f'Deleted Node data is: {temp.link.data}') # delete last node (the node next to where temp is point to)
        temp.link = None # make the link part of present node None
