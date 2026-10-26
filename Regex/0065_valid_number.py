# Complejidad temporal: O(1)
# Complejidad espacial: O(1)
# Justificación: El tiempo de ejecución está acotado por la longitud máxima de la cadena validada mediante una única expresión regular precompilada.

import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Expresión regular estricta para números enteros, decimales y notación científica (con 'e' o 'E')
        pattern = r"^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$"
        return bool(re.fullmatch(pattern, s))
