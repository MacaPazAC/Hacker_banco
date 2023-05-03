"""Hacker contraseña del banco
ingresa tu contraseña
pass = 4455
rango de la contaseña:
0000 ---> mínimo
9999 ---> máximo
(inicio, n+1)
Genera un for que recorra hasta encontrar el valor"""

print("Ingresa tu contraseña super segura:")
contrasena = int(input())
for clave in range(0000,10000):
    print(clave)
    if clave == contrasena:
        print("Hackeado")
        break