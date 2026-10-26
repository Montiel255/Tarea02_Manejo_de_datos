from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Lista donde iremos guardando los máximos de cada ventanita
        resultado = []
        
        # Cola doble (deque) para guardar los ÍNDICES de los números.
        # El rey (el número más grande) siempre estará a la izquierda (en la posición 0).
        deq = deque()
        
        for i in range(len(nums)):
            # 1. Jubilamos a los abuelos: si el índice que está hasta adelante 
            # ya se quedó fuera de nuestra ventana actual, lo sacamos por la izquierda.
            if deq and deq[0] < i - k + 1:
                deq.popleft()
            
            # 2. Destronamos a los débiles: si el número nuevo es más grande que 
            # los que están al final de la cola, los borramos porque ya no sirven de nada.
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()
            
            # 3. Metemos el índice del número actual al final de la fila
            deq.append(i)
            
            # 4. Si la ventanita ya tiene al menos tamaño 'k', guardamos el máximo 
            # (que siempre está asegurado en la primera posición de la cola: deq[0])
            if i >= k - 1:
                resultado.append(nums[deq[0]])
                
        return resultado
