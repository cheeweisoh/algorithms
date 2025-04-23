class Solution:
    def countLargestGroup(self, n: int) -> int:
        mem = {0: 0}
        counts = [0] * (4 * 9 + 1)

        for i in range(1, n+1):
            q, r = i // 10, i % 10
            mem[i] = r + mem[q]
            counts[mem[i]] += 1

        return counts.count(max(counts))
