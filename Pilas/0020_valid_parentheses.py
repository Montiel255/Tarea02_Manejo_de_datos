# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Se recorre la cadena de longitud n una sola vez y la pila puede almacenar hasta n elementos en el peor de los casos.

class Solution:
    def isValid(self, s: str) -> bool:
        pila = []
        mapeo = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapeo:
                # Sacar el elemento de la pila si no está vacía, de lo contrario asignar un valor dummy
                tope = pila.pop() if pila else '#'
                if mapeo[char] != tope:
                    return False
            else:
                pila.append(char)
                
        return not pila
