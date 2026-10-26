import re
class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        fracciones = re.findall(r"[+-]?\d+/\d+", expression)

        num_total = 0
        den_total = 1

        for fraccion in fracciones:
            partes = fraccion.split("/")
            numerador = int(partes[0])
            denominador = int(partes[1])

            num_total = (
                num_total * denominador
                + numerador * den_total
            )
            den_total = den_total * denominador

            divisor = self.mcd(abs(num_total), den_total)
            num_total //= divisor
            den_total //= divisor

        return str(num_total) + "/" + str(den_total)

    def mcd(self, a, b):
        while b:
            a, b = b, a % b
        return a