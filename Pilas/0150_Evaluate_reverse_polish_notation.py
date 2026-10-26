# Complejidad temporal: O(n)
# Complejidad espacial: O(n)
# Justificación: Se procesa cada elemento de la lista de tokens una vez, utilizando una pila para almacenar los operandos intermedios.

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        pila = []
        
        for t in tokens:
            if t not in "+-*/":
                pila.append(int(t))
            else:
                b = pila.pop()
                a = pila.pop()
                if t == '+':
                    pila.append(a + b)
                elif t == '-':
                    pila.append(a - b)
                elif t == '*':
                    pila.append(a * b)
                elif t == '/':
                    # División truncada hacia cero en Python
                    pila.append(int(a / b))
                    
        return pila[0]
