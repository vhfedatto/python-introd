#exercício 6 - Removendo valores
valores = [10, 20, 30, 40, 50]

for i in range(len(valores) -1, -1, -1):
    if valores[i] > 30:
        valores.pop(i)

print(valores)

