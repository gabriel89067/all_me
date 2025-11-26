import numpy as np
import matplotlib.pyplot as plt

# Defina os coeficientes da função: ax² + bx + c
a = 1
b = -3
c = -4

# Gera valores de x
x = np.linspace(-10, 10, 400)

# Calcula y = ax² + bx + c
y = a*x**2 + b*x + c

# Plota o gráfico
plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Gráfico da Função Quadrática")
plt.grid(True)

plt.show()
