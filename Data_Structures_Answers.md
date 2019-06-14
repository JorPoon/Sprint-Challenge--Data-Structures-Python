Add your answers to the questions below.

1. What is the runtime complexity of your ring buffer's `append` method?

O(1) because the item append is only one at a time or fixed amount at a time.

2. What is the space complexity of your ring buffer's `append` function?

O(1) because there is a fixed amount of capacity

3. What is the runtime complexity of your ring buffer's `get` method?

O(n) it contains a for loop that depends on the capacity of the data structure

4. What is the space complexity of your ring buffer's `get` method?

O(n) it depends on the size of data structure.

5. What is the runtime complexity of the provided code in `names.py`?

O(n ^ 2) there are 2 for loops in the provided code and it both depends on the size of the txt.file of names.

6. What is the space complexity of the provided code in `names.py`?

O(n) the space used is the amount it needs to fit the duplicate array.

7. What is the runtime complexity of your optimized code in `names.py`?

O(n) + O(n) = O(2n) = O(n) since I ran two loops that are not nested.
 
8. What is the space complexity of your optimized code in `names.py`?

O(n) requires the same space as provided code.

MVP DONE.
