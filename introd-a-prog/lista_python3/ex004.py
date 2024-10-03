#exercício 4 - Testando comandos em listas:
#comandos: .insert(), len(), .pop(), .remove(), .append(), .sort()
carros = ['Fiat', 'Chevrolet', 'Ford', 'Honda']
print(carros)

#Adicione a marca Jeep na segunda posição da lista:
carros.insert(2, 'Jeep')
print(carros)

#Apague o último registro da lista:
ultimo = len(carros)
ul = ultimo - 1
carros.pop(ul)
print(carros)

#Adicione a marca Toyota a última posição da lista:
carros.append('Toyota')
print(carros)

#Mostre quantos elementos possui a lista:
print(f'O tamanho da lista é {len(carros)}')

#Ordene a lista:
carros.sort()
print(carros)

