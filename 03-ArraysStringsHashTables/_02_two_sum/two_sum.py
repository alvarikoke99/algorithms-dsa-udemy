"""
Dado un array de números enteros y un target, retorna los índices de dos
números para los que la suma de ambos sea igual al target.

Puedes asumir que hay solamente una solución.

Ejemplo 1:
 Input: nums = [9,2,5,6], target = 7
 Output: [1,2]
 Explicación: nums[1] + nums[2] == 7, devolvemos [1, 2].

Ejemplo 2:
 Input: nums = [9,2,5,6], target = 100
 Output: null

O(N)
"""
from typing import List, Optional


class TwoSum:

    def two_sum(self, nums: List[int], target: int) -> Optional[List[int]]:
        if nums is None or len(nums) < 2:
            return None
        comp_map = dict()
        for i, value in enumerate(nums):
            if value in comp_map:
                return [comp_map.get(value), i]
            comp_map[target - value] = i
        return None