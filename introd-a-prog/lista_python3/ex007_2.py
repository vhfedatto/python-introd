#exercício 7 - itens duplicados
valores = [1, 1, 2, 2, 3, 4, 8, 9, 9]
sem = []

for i in valores:
    if i not in sem:
        sem.append(i)

print(valores)
print(sem)

