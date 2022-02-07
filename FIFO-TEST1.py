# I use python list in this project
class Queue:
    # function which list elements
    def __init__(self) :
        self.elements = []

    # function which manage enter elements elements
    def inqueue(self ,data):
        self.elements.append(data)
        return data
    
    # function which manage output elements
    def outqueue(self):
        self.elements.pop(0)
    
    # identify the last elelment in list
    def rear(self):
        return self.elements[-1]

    # identify the first elelment in list
    def front(self):
        return self.elements[0]
    
    # manage if the queue is empty
    def is_empty(self):
        return len(self.elements) == 0

if __name__ == '__main__':
        queue = Queue()
        # checking is_empty method -> True
        print("queue is empty:")
        print(queue.is_empty())

        # list queue
        queue.inqueue(1)
        queue.inqueue(2)
        queue.inqueue(3)
        queue.inqueue(4)
        queue.inqueue(5)
        queue.inqueue(6)
        queue.inqueue(7)
        queue.inqueue(8)

        # again checking is_empty method -> False
        print("queue is empty:")
        print(queue.is_empty())

        # printing the front and rear elements using front and rear methods respectively -> 1, 5
        print("front and rear elements are:")

        print(queue.front() , end ='   ')
        print(queue.rear())

        # printing the front and rear elements using front and rear methods respectively -> 1, 5
        print("front and rear elements are:")

        queue.outqueue()

        print(queue.front() , end ='   ')
        print(queue.rear())

        # printing the front and rear elements using front and rear methods respectively -> 1, 5
        print("front and rear elements are:")

        queue.outqueue()
        
        print(queue.front() , end ='   ')
        print(queue.rear())

        # printing the front and rear elements using front and rear methods respectively -> 1, 5
        print("front and rear elements are:")

        queue.outqueue()
        
        
        print(queue.front() , end ='   ')
        print(queue.rear())

        # removing all the elements

        queue.outqueue()
        queue.outqueue()
        queue.outqueue()
        queue.outqueue()
        queue.outqueue()

        # checking the is_empty method for the last time -> True
        print("queue is empty now:")
        print(queue.is_empty())
        


    