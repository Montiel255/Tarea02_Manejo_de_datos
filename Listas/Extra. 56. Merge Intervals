class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        # si no hay intervalos, regresamos una lista vacia
        if not intervals:
            return []
        
        # 1. Ordenamos los intervalos basandonos en su tiempo de inicio (el primer numero)
        intervals.sort(key=lambda x: x[0])
        
        # Lista donde iremos guardando los intervalos ya fusionados
        merged = []
        
        for interval in intervals:
            # Si la lista de fusionados esta vacia o el intervalo actual NO se encima con el ultimo guardado
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Si si se enciman, actualizamos el final del ultimo intervalo con el numero mas grande
                merged[-1][1] = max(merged[-1][1], interval[1])
                
        return merged
