

class Node:

  def __init__(self, data):
    self.data = data
    self.next = None

  def __str__(self):
    return str(self.data)

class SinglyLinkedList:
  
  def __init__(self):
    self.head = None

  def append(self, data):
    if self.head == None:
      self.head = Node(data)
      return
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    current_node.next = Node(data)

  def prepend(self, data):
    new_head = Node(data)
    new_head.next = self.head
    self.head = new_head

  def delete_with_value(self, data):
    if self.head == None:
      return
    if self.head.data == data:
      self.head = self.head.next
      return

    current_node = self.head
    while current_node.next != None:
      if current_node.next.data == data:
        current_node.next = current_node.next.next
        return
      current_node = current_node.next

  def print(self):
    if self.head == None:
      print('This singly linked list is empty')
      return
    current_node = self.head
    while current_node.next != None:
      print(f'{current_node.data} -- > {current_node.next.data}')
      current_node = current_node.next
    print(current_node.data)
    return
    

singlyLinkedList = SinglyLinkedList()

singlyLinkedList.print()

headNode = Node(1)
singlyLinkedList.append(headNode)

for i in range(2, 4):
  singlyLinkedList.append(Node(i))

singlyLinkedList.print()

