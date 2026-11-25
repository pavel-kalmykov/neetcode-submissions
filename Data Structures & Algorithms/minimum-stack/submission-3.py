class MinStack:
    def __init__(self):
        self.st = []
        self.minSt = []

    def push(self, x):
        self.st.append(x)
        
        # If minSt is empty or new element is smaller than 
        # the top of minSt, push it
        if not self.minSt or x <= self.minSt[-1]:
            self.minSt.append(x)
        else:
        
            # Otherwise, repeat the top of minSt 
            self.minSt.append(self.minSt[-1])

    # Pop the top element
    def pop(self):
        if not self.st:
            return
        self.st.pop()
        self.minSt.pop()

    # Return top element
    def top(self):
        if not self.st:
            return -1
        return self.st[-1]

    # Get the minimum element
    def getMin(self):
        if not self.minSt:
            return -1
        return self.minSt[-1]
