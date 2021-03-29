

class MaxHeap:

  def __init__(self, capacity=10, size=0):
    self.capacity = capacity
    self.size = size
    self.heap_array = []

  def get_left_child_index(self, parent_index):
    return 2 * parent_index + 1

  def get_right_child_index(self, parent_index):
    return 2 * parent_index + 2

  def get_parent_index(self, child_index):
    return int((child_index - 1) / 2)

  def has_left_child(self, index):
    return bool(self.get_left_child_index(index) < self.size)

  def has_right_child(self, index):
    return bool(self.get_right_child_index(index) < self.size)

  def has_parent(self, index):
    return bool(self.get_parent_index(index) < self.size)

  def get_left_child(self, index):
    return self.heap_array[self.get_left_child_index(index)]

  def get_right_child(self, index):
    return self.heap_array[self.get_right_child_index(index)]

  def get_parent(self, index):
    return self.heap_array[self.get_parent_index(index)]

  def swap(self, indexOne, indexTwo):
    _temp = self.heap_array[indexOne]
    self.heap_array[indexOne] = self.heap_array[indexTwo]
    self.heap_array[indexTwo] = _temp

  
  def peek(self):
    if self.size == 0:
      console.log("Heap is empty")
      return None
    return self.heap_array[0]

  def pull(self):
    if self.size == 0:
      console.log("Heap is empty")
      return None
    result = self.heap_array.pop(0) # Get root value
    self.heap_array.insert(0, self.heap_array.pop()) # Get lastest value and insert at root index
    self.size -= 1
    self.heapify_down() # Sort from top
    return result

  def add(self, value):
    self.heap_array.append(value)
    self.size += 1
    self.heapify_up() # Sort from bottom
    return

  def heapify_up(self):
    index = self.size - 1
    # While the element has a parent and that parent's value is less than the elements value
    while self.has_parent(index) and self.get_parent(index) < self.heap_array[index]:
      parent_index = self.get_parent_index(index)
      self.swap(index, parent_index)
      index = parent_index

    return

  def heapify_down(self):
    index = 0
    # While the element has a left child
    while self.has_left_child(index):

      larger_child_index = self.get_left_child_index(index)

      if self.has_right_child(index) and self.get_right_child(index) > self.get_left_child(index):
        larger_child_index = get_right_child_index(index)

      if self.heap_array[index] > self.heap_array[larger_child_index]:
        break
      else:
        self.swap(index, larger_child_index)
      
      index = larger_child_index

    return
    
  
maxheap = MaxHeap()

maxheap.add(2)
maxheap.add(15)
maxheap.add(3)

print(maxheap.peek())
print(maxheap.pull())
print(maxheap.heap_array)

maxheap.add(1)
print(maxheap.peek())

print(maxheap.heap_array)
print(maxheap.size)

maxheap.add(15)
print(maxheap.peek())

print(maxheap.heap_array)

