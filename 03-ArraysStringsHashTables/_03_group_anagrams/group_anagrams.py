"""
Un anagrama es una palabra creada a partir de la reordenación de las letras de otra palabra. Ej: saco - caso
Dado un array de strings, devuelve los anagramas agrupados. Cualquier orden es válido.

Ejemplo:
 Input: words = ["saco", "arresto", "programa", "rastreo", "caso"].
 Output: [["saco", "caso"], ["arresto", "rastreo"], ["programa"]].
"""
from typing import List

from pygments.lexer import words


class GroupAnagrams:

    def group_anagrams(self, words: List[str]) -> List[List[str]]:
        if words is None or len(words) == 0:
            return []

        hash_map = dict()
        for word in words:
            identifier = self.get_anagram_hash(word)
            if identifier not in hash_map:
                hash_map[identifier] = []
            hash_map.get(identifier).append(word)

        return list(hash_map.values())

    def get_anagram_map(self, word: str) -> dict:
        letters = dict()
        for char in word:
            letters[char] = letters.get(char, 0) + 1
        return letters

    def get_anagram_hash(self, word: str) -> str:
        letters = [0] * 26
        for char in word:
            letters[ord(char) - ord('a')] += 1
        return "".join(map(str, letters))