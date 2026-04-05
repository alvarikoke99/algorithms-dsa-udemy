from typing import Dict, Optional


class TrieNode:
    def __init__(self):
        self.children: Dict[str, 'TrieNode'] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self, ignore_case = True):
        self.root = TrieNode()
        self.ignore_case = ignore_case

    def insert(self, word: str) -> None:
        current_node = self.root
        target_word = word.lower() if self.ignore_case else word

        for c in target_word:
            child = current_node.children.get(c)
            if child is None:
                child = TrieNode()
                current_node.children[c] = child
            current_node = child

        current_node.is_end_of_word = True

    def search(self, prefix: str) -> bool:
        current_node = self.root
        target_prefix = prefix.lower() if self.ignore_case else prefix
        
        for c in target_prefix:
            current_node = current_node.children.get(c)
            if current_node is None:
                return False

        return True
