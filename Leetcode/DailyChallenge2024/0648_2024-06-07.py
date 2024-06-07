class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]

        node.isEnd = True

    def searchRoot(self, word):
        node = self.root
        prefix = ""

        for char in word:
            if char not in node.children:
                break
            node = node.children[char]
            prefix += char
            if node.isEnd:
                return prefix

        return word


class Solution:
    def replaceWords(self, dictionary: list[str], sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        words = sentence.split()
        replacedWords = [trie.searchRoot(word) for word in words]

        return " ".join(replacedWords)
