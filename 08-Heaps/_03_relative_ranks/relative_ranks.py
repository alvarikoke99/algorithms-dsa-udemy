from typing import List
import heapq


"""
Recibes un array de puntuaciones, en el que el valor de la posición i se corresponde
con la puntuación del participante i. No puede haber puntuaciones repetidas.

Devuelve un array con la posición obtenida por cada participante, dando medallas a los
tres primeros.

Ejemplo 1:
 Input: [5,4,3,2,1]
 Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]

Ejemplo 2:
 Input: [10,3,8,9,4]
 Output: ["Gold Medal","5","Bronze Medal","Silver Medal","4"]
"""


class RelativeRanks:
    def find_relative_ranks(self, score: List[int]) -> List[str]:
        max_heap = []
        output = [0] * len(score)

        for index, num in enumerate(score):
            heapq.heappush(max_heap, (-num, index))

        cont = 1
        while max_heap:
            _, pos = heapq.heappop(max_heap)
            
            match cont:
                case 1:
                    place = "Gold Medal"
                case 2:
                    place = "Silver Medal"
                case 3:
                    place = "Bronze Medal"
                case _:
                    place = str(cont)

            cont += 1
            output[pos] = place
        
        return output