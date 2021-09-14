My task was to implement dynamic data structure called **Binary Search Tree**
My implementation in python provides such interface:
    1. __init__(self, key=lambda x: x) - constructor with possibility to provide custom way of sorting elements
    2. insert(self, data) - add element
    3. delete(self, key, delete_all=True) - delete single element or all if they are in BST
    4. min(self) - find smallest element
    5. max(self) - find greatest element
    6. delete_min(self, delete_all=True) - delete single or all smallest elements
    7. delete_max(self, delete_all=True) - delete single or all geratest elements
    8. clear(self) - delete all elements from BST
    9. size(self) - get number of elements in BST
    10. operator in - check if element is in BST
    11. count(self, key) - get number of occurrences of element in BST
    12. items(self) - get list of elements in BST
    13. rank(self, key) - get number of elements smaller than the key
    14. floor(self, key) - find greatest element not greater than the key
    15. ceiling(self, key) - find smallest element not smaller then the key

To run:
    1. Make sure You have python installed
    2. Download or clone the repository
    3. Navigate to that folder
    4. Open cmd in that folder
    5. Type **"python main.py"**

To run test:
    1. Make sure You have coverage installed
    2. In file "test_main.py" replace path with the path to Your folder
    3. Type **"python test_main"**
