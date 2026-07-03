
class LinkedList:
    
    def __init__(self):
        self.linkedList = []
        self.length = 0
    def get(self, index: int) -> int:
        if self.length>=index+1:
            return self.linkedList[index]
        else:
            return -1
    def insertHead(self, val: int) -> None:
        self.linkedList.insert(0, val)
        self.length += 1

    def insertTail(self, val: int) -> None:
        self.linkedList.append(val)
        self.length += 1

    def remove(self, index: int) -> bool:
        if index+1<= self.length:
            self.linkedList.pop(index)
            self.length -= 1
            return True
        else:
            return False

    def getValues(self) -> List[int]:
        return self.linkedList
