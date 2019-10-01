Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> class MinStack:

    def __init__(self):
        self.items=[]
        self.min_stack=[]
            
        """
        initialize your data structure here.
        """
        

    def push(self, x: int) -> None:
        self.items.append(x)
        if not self.min_stack:
            self.min_stack.append(x)
        else:
            self.min_stack.append(x) if x < self.min_stack[-1] else self.min_stack.append(self.min_stack[-1])          
    def pop(self) -> None:
        self.min_stack.pop()
        return self.items.pop()
    def top(self) -> int:
        return self.items[-1] 
    def getMin(self)->int: 
        return self.min_stack[-1]
