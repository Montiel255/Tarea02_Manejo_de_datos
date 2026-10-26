#Complejidad temporal O(n)
#Complejidad espacial O(n)
#Porque recorre la lista dos veces
#Contando la lista resultados 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        resultado = [1] * len(nums)

        producto = 1
        for i in range(len(nums)):
            resultado[i] = producto
            producto *= nums[i]

        producto = 1
        for j in range(len(nums) - 1, -1, -1):
            resultado[j] *= producto
            producto *= nums[j]

        return resultado
