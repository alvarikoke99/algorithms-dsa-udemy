from typing import List


"""
Dada una lista de proyectos y las dependencias entre ellos, devuelve un orden de
compilación válido para dichos proyectos.

La lista de dependencias es una lista de pares de strings (a, b), que indican que el
proyecto b depende del a (el a debe ser compilado con antelación).

Ejemplo 1:
 Input:
   projects: a, b, c, d
   dependencies: [(a, b), (a, c), (a, d), (c, b), (d, b), (d, c)]
 Output: a, d, c, b

Ejemplo2:
 Input:
   projects: a, b, c, d
   dependencies: [(a, b), (b, c), (c, d), (d, a)]
 Output: Lanza excepción. No se puede construir ya que se forma un ciclo.
"""


class BuildOrder:
    def build_order(self, projects: List[str], dependencies: List[List[str]]) -> List[str]:
        raise NotImplementedError("Not implemented yet")
