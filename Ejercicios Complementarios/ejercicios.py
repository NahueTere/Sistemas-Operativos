import math
pi=3.1416

#Ejercicio 1
r = int(input("Ingrese radio de la esfera (mm): "))
v = (4/3)*pi*(r**3)
#print(f"Volumen= {round(v,2)}mm")

#Ejercicio 2
h = int(input("Ingrese altura del triangulo (mm): "))
p = 3*(2*h/3**0.5)
print(f"Perimetro= {round(p,2)}mm")

#Ejercicio 3
soles = float(input("Cuantos soles tenes?: "))
d = soles/3.25
e = soles/3.83
print(f"Equivalente en dolares: {d}")
print(f"Equivalente en euros: {e}")

#Ejercicio 4
m = float(input("Metros: "))
s = float(input("Segundos: "))
v = m/s
print(f"{round(v,2)}m/s")

#Ejercicio 5
p = float(input("Precio por unidad: "))
d = int(input("Cantidad de docenas: "))
pt = d*12*p
print(f"Precio a pagar: {pt}")

#Ejercicio 6
millas = int(input("Millas: "))
km = millas*1.609344
print(f"Igual a {km}km")

#Ejercicio 7
print("Ingrese lados del triángulo:")
b = float(input("Lado b: "))
c = float(input("Lado c: "))
alfa = float(input("Ingrese el ángulo en grados sexagesimales: "))
a = ( b**2 + c**2 - 2*b*c * math.cos( alfa*pi/180 ) )**0.50
print(f"Lado a = {round(a,2)}")

#Ejercicio 8
va = float(input("Velocidad del movil a (m/s): "))
vb = float(input("Velocidad del movil b (m/s): "))
d = float(input("Distancia (m): "))
t = d/(va+vb)
print(f"se encontraran en {t}s")

#Ejercicio 9
x = float(input("Ingrese ángulo en radianes:"))
sex = x*180/pi
cen = x*200/pi
print("En sexagesimales es:", sex)
print("En centesimales es:", cen)

#Ejercicio 10
print("Ingrese valores del punto A(x1, y1 y z1)(mm): ")
x1 = float( input("x1: "))
y1 = float( input("y1: "))
z1 = float( input("z1: "))

print("Ingrese valores del punto B(x2, y2 y z2)(mm): ")
x2 = float( input("x2: "))
y2 = float( input("y2: "))
z2 = float( input("z2: "))

dis = ( (z2-z1)**2 + (y2-y1)**2 + (x2-x1)**2 )**0.5
print(f"La distancia entre los puntos es de {dis}")