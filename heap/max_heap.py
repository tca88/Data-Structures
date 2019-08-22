class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    self._bubble_up(len(self.storage) - 1)

  def delete(self):
    last_index = self.get_size()-1
    self.storage[0], self.storage[last_index] = self.storage[last_index], self.storage[0]
    deleted = self.storage.pop()
    self._sift_down(0)
    return deleted

  def get_max(self):
    return self.storage[0] # Or 1 if you decide to do the 1 index method

  def get_size(self):
    # Traverse through and count all of the elements
    # This an array - len(self.storage)
    # For stretch practice, do this with a traversal similar to BST
    return len(self.storage)

  def _bubble_up(self, index):
    # Helper function to compare to parent node and switch if appropriate
    if index == 0:
      return
    while (self.storage[index] > self.storage[(index-1) // 2] and index > 0):
      self.storage[index], self.storage[(index-1) // 2] = self.storage[(index-1) // 2], self.storage[index]
      index = (index-1) // 2

  def _sift_down(self, index):
    left_child = 2*index+1
    right_child = 2*index+2
  
    if left_child < self.get_size():
      if right_child < self.get_size():
          if self.storage[right_child] > self.storage[left_child]:
              left_child = right_child
          if self.storage[index] < self.storage[left_child]:
              self.storage[index], self.storage[left_child] = self.storage[left_child], self.storage[index]
              self._sift_down(left_child)

