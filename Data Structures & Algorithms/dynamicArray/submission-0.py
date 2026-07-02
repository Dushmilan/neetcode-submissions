class DynamicArray:
    def __init__(self, capacity: int):
        if capacity > 0:
            self.arr = [0] * capacity
        else:
            self.arr = []
        self.arr_ele = 0  # Number of actual elements

    def get(self, i: int) -> int:
        if i < 0 or i >= self.arr_ele:
            raise IndexError("Index out of bounds")
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        if i < 0 or i >= self.arr_ele:
            raise IndexError("Index out of bounds")
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        # If array is full, resize
        if self.arr_ele == len(self.arr):
            self.resize()
        
        # Add element at the end
        self.arr[self.arr_ele] = n
        self.arr_ele += 1

    def popback(self) -> int:
        if self.arr_ele == 0:
            raise IndexError("Cannot pop from empty array")
        self.arr_ele -= 1
        return self.arr[self.arr_ele]

    def resize(self) -> None:
        capacity = len(self.arr)
        if capacity == 0:
            self.arr = [0] * 1
        else:
            self.arr.extend([0] * capacity)

    def getSize(self) -> int:
        return self.arr_ele
    
    def getCapacity(self) -> int:
        return len(self.arr)