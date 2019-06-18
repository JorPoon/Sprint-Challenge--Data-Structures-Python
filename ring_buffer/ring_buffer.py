class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
    #establish the oldest element in the buffer
    #adds in new item
    #replace new item with oldest element
    self.storage[self.current] = item
    self.current += 1
    if self.current == self.capacity:
      self.current = 0

  def get(self):
    #search through list for "None"
    #Return data by slicing out None
    for i in range(len(self.storage)):
      if self.storage[i] == None:
        return self.storage[:i]
    return self.storage