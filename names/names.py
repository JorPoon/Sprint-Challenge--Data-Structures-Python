import time

class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    #check if the value being inserted is less than current value (left)
    if value < self.value:
      #check if the left child node has spot, if it does not place a new tree
      if not self.left:
        self.left = BinarySearchTree(value)
      #if it does, rerun the function for the next spot
      else:
        self.left.insert(value)
    #check if value being inserted is greater than current value (right)
    elif value >= self.value:
      #check if the right child node has spot open
      if not self.right:
        self.right = BinarySearchTree(value)
        #repeat process if spot is not empty
      else:
        self.right.insert(value)

    

  def contains(self, target):
    #checks if target is less than value then repeat check
    # checks if target is greater than value then repeat check
    # checks if target equal to value
    # if no value == target return false

    if self.value == target:
      return True
    elif self.value > target:
      if self.left is None:
        return False
      return self.left.contains(target)
    elif self.value < target:
      if self.right is None:
         return False
      return self.right.contains(target)

    


start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []

BinaryTest = BinarySearchTree('new_name')
for i in names_1:
    BinaryTest.insert(i)

for j in names_2:
    if BinaryTest.contains(j):
        duplicates.append(j)

# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

