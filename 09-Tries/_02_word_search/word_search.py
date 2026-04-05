from typing import List, Dict

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

"""
Dado un tablero m x n y un array de palabras, retorna todas las palabras existentes en el tablero.
Las palabras se pueden formar con caracteres horizontales o verticales, y un caracter no puede ser
usado múltiples veces en una palabra.

Ejemplo:
 Input:
   [
     ["p","e","r","o"]
     ["a","t","a","e"]
     ["t","e","l","v"]
     ["o","f","l","v"]
   ]

   words = ["pero","pato","comida", "veo", "pata"]

 Output: ["pero","pato", "veo", "pata"]
"""


class WordSearch:
    def find_words(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        columns = len(board[0])
        pass
    
    def build_trie(self, words: List[str], max_len: int) -> TrieNode:
        trie = Trie()
        for word in words:
          if len(word) <= max_len:
              trie.insert(word)
        return trie.root
          
