from typing import Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current_node = self.root
        lowercase_word = word.lower()

        for c in lowercase_word:
            child = current_node.children.get(c)
            if child is None:
                child = TrieNode()
                current_node.children[c] = child
            current_node = child

        current_node.is_end_of_word = True

    def search(self, prefix: str) -> bool:
        current_node = self.root
        prefix_lowercase = prefix.lower()

        for c in prefix_lowercase:
            current_node = current_node.children.get(c)
            if current_node is None:
                return False

        return True
