#Complejidad temporal: O(n)
#Complejidad espacial: O(n)
#Recorre la lista una vez y las busquedas en diccionario son O(1)
#El diccionario puede almacenar n elementos
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        indices = {}
        for i in range(len(nums)):
            numero_actual = nums[i]
            complemento = target - numero_actual
    
            if complemento in indices:
                return [indices[complemento], i]
            indices[numero_actual] = i