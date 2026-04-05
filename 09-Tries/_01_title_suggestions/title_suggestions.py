from typing import List, Dict, Optional

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
Implementa un método que reciba un array de títulos de libros, un array con prefijos de búsqueda
y que devuelva un array indicando si existen libros con esos prefijos o no.

También se indicará si las mayúsculas y minúsculas son tratadas como iguales con un parámetro.

Ejemplo 1:
 Input:
   books: ["Whatever", "Book 1", "water", "Book 35"]
   prefixes: ["Wo", "Wa", "Boo", "fr"]
   ignoreCase: false

 Output:
   [false, false, true, false]

Ejemplo 2:
 Input:
   books: ["Whatever", "Book 1", "water", "Book 35"]
   prefixes: ["Wo", "Wa", "Boo", "fr"]
   ignoreCase: true

 Output:
   [false, true, true, false]
"""


class TitleSuggestions:
  def title_suggestions(self, books: List[str], prefixes: List[str], ignore_case: bool) -> List[bool]:
    trie = Trie(ignore_case)   
    results = []   

    for book in books:
      trie.insert(book)

    for prefix in prefixes:
      results.append(trie.search(prefix))

    return results