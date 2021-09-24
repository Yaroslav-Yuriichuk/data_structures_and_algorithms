**My task was to implement dynamic data structure called **Binary Search Tree**.**  

**My implementation in python provides such interface:**  
    1. \_\_init__(self, key=lambda x: x) - constructor with possibility to provide custom way of sorting elements.  
    2. \_\_str__(self) - print BST (elements in ascending order)  
    3. insert(self, data) - add element.  
    4. delete(self, key, delete_all=True) - delete single element or all if they are in BST.  
    5. min(self) - find smallest element.  
    6. max(self) - find greatest element.  
    7. delete_min(self, delete_all=True) - delete single or all smallest elements.  
    8. delete_max(self, delete_all=True) - delete single or all geratest elements.  
    9. clear(self) - delete all elements from BST.  
    10. size(self) - get number of elements in BST.  
    11. operator in - check if element is in BST.  
    12. count(self, key) - get number of occurrences of element in BST.  
    13. items(self) - get list of elements in BST.  
    14. rank(self, key) - get number of elements smaller than the key.  
    15. floor(self, key) - find greatest element not greater than the key.  
    16. ceiling(self, key) - find smallest element not smaller then the key.
    17. print_in_ascii(self) - draw tree in ascii praphics  
    
**To run:**  
    1. Make sure You have python installed.  
    2. Download or clone the repository.  
    3. Navigate to that folder.  
    4. Open cmd in that folder.  
    5. Type **"python main.py"**.  
    
**To run tests:**  
    1. Make sure You have coverage installed.  
    2. In file "test_main.py" replace path with the path to Your folder.  
    3. Type **"python test_main"**.  

    
