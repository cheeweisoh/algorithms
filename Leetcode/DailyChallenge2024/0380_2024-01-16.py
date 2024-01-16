import random

class RandomizedSet:
    def __init__(self):
        self.rset = {}
    
    def insert(self, val: int) -> bool:
        if val not in self.rset.keys():
            self.rset[val] = 1
            return True
        return False
    
    def remove(self, val: int) -> bool:
        if val in self.rset.keys():
            self.rset.pop(val)
            return True
        return False
    
    def getRandom(self) -> int:
        choices = list(self.rset.keys())
        return random.choice(choices)