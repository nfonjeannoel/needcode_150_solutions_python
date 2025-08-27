class WordDictionary:

    def __init__(self):
        self.words = []

    def addWord(self, word: str) -> None:
        self.words.append(word)

    def search(self, word: str) -> bool:
        for w in self.words:
            if len(word) != len(w):
                continue

            i = 0
            while i < len(w):
                if w[i] == word[i] or word[i] == '.':
                    i += 1
                else:
                    break

            if i == len(w):
                return True
        return False


class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class WordDictionary2:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for w in word:
            if w not in cur.children:
                cur.children[w] = TrieNode()
            cur = cur.children[w]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root

            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.isEndOfWord

        return dfs(0, self.root)
