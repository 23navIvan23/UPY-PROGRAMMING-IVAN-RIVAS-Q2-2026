import math

# INPUT
a = input("Write the left endpoint of the interval: ")
b = input("Write the right endpoint of the interval: ")
f_x = input("Write the function to integrate: ")
method = input("Write the integration method (LRM/RRM/MRM/TRAP): ")

# PROCESS
# Evaluar si la entrada es "pi" o un número flotante estándar
if "pi" in a:
    a = math.pi
else:
    a = float(a)

if "pi" in b:
    b = math.pi
else:
    b = float(b)

n = 1000
h = (b - a) / n
area = 0.0
shift = 0
constant = 0

# Configuración de variables según el método seleccionado
if method == "RRM":
    shift = 1

if method == "MRM":
    constant = h / 2

# Estructura de cálculo
if method == "TRAP":
    variable = 1
    f_0 = f_x.replace("x", str(a))
    area += (h / 2) * eval(f_0)
    
    for i in range(variable, n):
        xi = a + i * h
        f_xi = f_x.replace("x", str(xi))
        area += (h / 2) * 2 * eval(f_xi)
        
    f_xn = f_x.replace("x", str(b))
    area += (h / 2) * eval(f_xn)

else:
    # Este bloque ejecuta LRM, RRM y MRM
    for i in range(shift, n + shift):
        xi = a + i * h
        height = f_x.replace("x", str(xi + constant))
        area += h * eval(height)

# OUTPUT
print(f"The integration of {f_x} is {area}")