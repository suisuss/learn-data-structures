
class Node:

  def __init__(self, data):
    self.data = data
    self.next = None
    self.previous = None

  def __str__(self):
    return str(self.data)


class DoublyLinkedList:

  def __init__(self):
    self.head = None

  def append(self, data):
    if self.head == None:
      self.head = Node(data)
      return
    current_node = self.head
    while current_node.next != None:
      current_node = current_node.next
    new_node = Node(data)
    current_node.next = new_node
    new_node.previous = current_node
    return

  def prepend(self, data):
    if self.head == None:
      self.head = Node(data)
      return

    new_head_node = Node(data)
    new_head_node.next = self.head
    self.head.previous = new_head_node
    self.head = new_head_node
    return

  def delete_with_value(self, data):
    if self.head == None:
      return
    if self.head.data == data:
      self.head.next.previous = None
      self.head = self.head.next
      return
    current_node = self.head
    while current_node.next != None:
      if current_node.next.data == data:
        current_node.next = current_node.next.next
        current_node.next.previous = current_node
        return
      current_node = current_node.next
    return

  def print(self):
    if self.head == None:
      print('This doubly linked list is empty')
      return
    current_node = self.head
    while current_node.next != None:
      print(f'{current_node.data} < -- > {current_node.next.data}')
      current_node = current_node.next
    return


doublyLinkedList = DoublyLinkedList()

doublyLinkedList.append(1)

doublyLinkedList.prepend(2)

doublyLinkedList.print()

print('\n')

for i in range(3, 5):
  doublyLinkedList.append(i)

doublyLinkedList.print()

print('\n')

doublyLinkedList.delete_with_value(2)

doublyLinkedList.print()