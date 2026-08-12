class Node:
    def _init_(self,data):
        self.data=data
        self.next=None
front=None
rear=None
def enqueue(value):
    global front,rear
    new_node=Node(value)
    new_node.next=None
    if rear is None:
        front=new_node
        rear=new_node
    else:
        rear.next=new_node
        rear=new_node
    print(f"Car '{value}' entered the parking queuee")
def dequeue():
    global front,rear
    if front is None:
        print("Queue is Empty")
        return
    temp=front
    front=front.next
    print(f"Car '{temp.data}' exited the parking queue")
    del temp
    if front is None:
        rear=None
def show():
    if front is None:
        print(f"Queue is Empty")
        return
    temp=front
    print("Cars current in queue:",end=" ")…
