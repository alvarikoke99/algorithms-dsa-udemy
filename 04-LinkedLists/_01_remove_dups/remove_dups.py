from single_linked_list import Node


"""
Escribe un algoritmo para eliminar los elementos duplicados en una Lista enlazada

Ejemplo:
 Input: 1->2->2->3->4->1
 Output: 1->2->3->4
 
Temporal: O(N)
Espacial: O(N)

Follow-up: ¿Cuál sería tu solución si no pudieras utilizar memoria adicional?
- Iterando el array con cada valor
Temporal: O(N^2)
Espacial: O(1)
"""


class RemoveDups:

    def remove_dups(self, head: Node) -> None:
        if head is None or head.value is None:
            return

        current = head
        visited = {head.value}

        while current.next:
            visited.add(current.value)
            if current.next.value in visited:
                current.next = current.next.next
            current = current.next