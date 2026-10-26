# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Cada índice entra y sale de la pila monótona exactamente una vez, lo que garantiza un tiempo lineal.

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        resultado = [0] * n
        pila = []  # Almacena índices de días con temperaturas pendientes de superar
        
        for i, temp in enumerate(temperatures):
            while pila and temperatures[pila[-1]] < temp:
                indice_previo = pila.pop()
                resultado[indice_previo] = i - indice_previo
            pila.append(i)
            
        return resultado
