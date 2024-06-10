import collections
import math
import itertools
import heapq

################################## DATA STRUCTURE ###################################


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def createLinkedList(linked_data):
    reverse_data = linked_data[::-1]
    curr_node, prev_node = ListNode(reverse_data[0]), None
    for i in reverse_data[1:]:
        curr_node, prev_node = ListNode(i, curr_node), curr_node
    head = curr_node
    return head


def printLinkedList(head):
    ans = []
    while head is not None:
        ans.append(head.val)
        head = head.next
    return ans


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def createTree(nodeList, index):
    root = TreeNode(nodeList[index])

    if 2 * index + 1 < len(nodeList):
        root.left = createTree(nodeList, 2 * index + 1)
    if 2 * index + 2 < len(nodeList):
        root.right = createTree(nodeList, 2 * index + 2)

    return root


nodeList = [1, 2, 3, 4, 5]
root = createTree(nodeList, 0)

####################################################################################


class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        rounds = k // (n - 1)
        rem = k % (n - 1)
        ans = 0

        if rounds % 2 == 0:
            ans = rem
        else:
            ans = n - rem - 1

        return ans


print("Question 1")
soln = Solution()
print(soln.numberOfChild(3, 5))
print(soln.numberOfChild(5, 6))
print(soln.numberOfChild(4, 2))


####################################################################################


class Solution:
    def valueAfterKSeconds(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        state = [1] * n

        for i in range(k):
            for j in range(1, len(state)):
                state[j] = state[j] + state[j - 1]

        return state[-1] % MOD


print("\nQuestion 2")
soln = Solution()
print(soln.valueAfterKSeconds(4, 5))
print(soln.valueAfterKSeconds(5, 3))


####################################################################################


class Solution:
    def maxTotalReward(self, rewardValues: list[int]) -> int:
        n = len(rewardValues)
        rewardValues.sort(reverse=True)  # Sort in descending order
        dp = [0] * n
        dp[0] = rewardValues[0]
        total_reward = rewardValues[0]

        for i in range(1, n):
            curr_reward = rewardValues[i]
            if curr_reward > total_reward:
                max_prev = 0
                for j in range(i):
                    max_prev = max(max_prev, dp[j])
                dp[i] = max_prev + curr_reward
                total_reward = curr_reward
            else:
                dp[i] = total_reward

        return max(dp)


print("\nQuestion 3")
soln = Solution()
print(soln.maxTotalReward([1, 1, 3, 3]))
print(soln.maxTotalReward([1, 6, 4, 3, 2]))


####################################################################################


class Solution:
    pass


print("\nQuestion 4")
soln = Solution()
