"""
Dado un método que recibe una String, comprobar si todos los caracteres son únicos o no.

isUnique("abcde") => true;
isUnique("abcded") => false;
"""


class IsUnique:

    def is_unique(self, s: str) -> bool:
        checked = set()
        for char in s:
            if char in checked:
                return False
            checked.add(char)
        return True