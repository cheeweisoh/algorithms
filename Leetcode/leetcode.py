import collections
import math
import random
import heapq
import string
import bisect
from structures import *

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next

def main():
    pass

if __name__ == "__main__":
    main()
