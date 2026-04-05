from typing import List
import heapq

"""
Diseña una clase para obtener el kth elemento más grande de un stream de datos.

KthLargest(int k, int[] nums) Inicializa el objecto con el valor de K y con el conjunto de datos.
int add(int val) Añade un nuevo elemento y devuelve el kth mayor actual.

Ejemplo:
 Input:
   k = 4
   nums = [1, 2, 3, 4, 5]

 Output:
   add(6) = 3
   add(1) = 3
   add(8) = 4
"""


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
      self.k = k
      self.min_heap = nums
      heapq.heapify(self.min_heap)
      
      while len(self.min_heap) > k:
        heapq.heappop(self.min_heap)
          
    def add(self, val: int) -> int:
      heapq.heappush(self.min_heap, val)

      if len(self.min_heap) > self.k:
        heapq.heappop(self.min_heap)
        
      return self.min_heap[0]