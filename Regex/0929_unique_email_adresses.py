#Complejidad temporal: O(nm)
#Complejidad espacial: O(nm)
#Limpiamos n correos de longitud m
#En el peor caso porque guardamos los correos unicos
import re
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        unicos = set ()
        for email in emails:    
            partes = email.split("@")
            usuario = partes[0]
            dominio = partes[1]
            usuario_limpio = re.sub(r"\+.*", "", usuario)
            usuario_limpio = re.sub(r"\.", "", usuario_limpio)
            emails_limpios = usuario_limpio + "@" + dominio
            unicos.add(emails_limpios)
        return len(unicos)