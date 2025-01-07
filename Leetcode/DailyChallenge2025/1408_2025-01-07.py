class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        """
        time complexity = O(n^2 * m)

        nested for-loop = O(n^2)
        find = O(m), m is the average length of words in words
        """
        words.sort(key=lambda x: len(x), reverse=True)
        res = set()
        n = len(words)

        for i in range(n):
            for j in range(i + 1, n):
                if words[i].find(words[j]) != -1:
                    res.add(words[j])

        return list(res)
