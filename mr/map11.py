import sys
import re

for linea in sys.stdin:
        claves = linea.split()
        for palabra in claves:
                palabrafilt = re.sub(r'[\W_]+', '', palabra.lower())
                longitud = "Longitud-" + str(len(palabrafilt))
                print(longitud, "1")
