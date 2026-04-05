from typing import List
import heapq
from collections import defaultdict


"""
Dado un conjunto de elementos y un valor k, devuelve los K elementos más frecuentes.
Se pueden devolver en cualquier orden.

Ejemplo:
 Input:
   nums = [1,1,1,2,2,3]
   k = 2

 Output:
   [1,2]

Input:
   nums = [1,1,2,2,3,3,3]
   k = 1

 Output:
   [3]

 O(N) + O(log C) + O(k * log C) -> O(N + K * (2)log C)
"""


class TopKFrequent:
    def top_k_frequent(self, nums: List[int], k: int) -> List[int]:
      frequencies = defaultdict(int)

      for n in nums:
        frequencies[n] += 1

      top_k = heapq.nlargest(k, frequencies, frequencies.get)
      return top_k