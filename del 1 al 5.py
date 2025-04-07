import math
"""Ejercicio 1
V = float(input("Velocidad (M/s): "))
T = int(input("Tiempo (s): "))
print("El movil se movilizó por",V*T,"metros")"""

"""Ejercicio 2
N1 = float(input("Primer Nota: "))
N2 = float(input("Segunda Nota: "))
N3 = float(input("Tercer Nota: "))
print("Su promedio es de: ",((N1+N2+N3)/3))"""

"""Ejercicio 3
Rc = int(input("Respuestas correctas: "))
Ri = int(input("Respuestas icorrectas: "))
Rb = int(input("Respuestas en blanco: "))
Rcf = Rc*3
Rif = Ri*-1
Rbf = Rb*0
Pf = Rcf+Rif+Rbf
print("Puntaje final:",Pf)"""

"""Ejercicio 4
Pg = int(input("Partidos ganados: "))
Pe = int(input("Partidos empatados: "))
Pp = int(input("Partidos perdidos: "))
Pgf = Pg*3
Ppf = Pp*0
Pf = Pgf+Pe+Ppf
print("Puntaje final:",Pf)"""

"""Ejercio 5"""
t = float(input("Ingrese el tamaño para la copia: "))
D = 1.44
Gb = 1024
Dr = (Gb*t)/D
print("Se requiere",math.ceil(Dr),"discos")