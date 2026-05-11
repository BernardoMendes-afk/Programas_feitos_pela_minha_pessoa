L = []
V = []
while True:
 lista1 = input("Digite um valor para 1ª lista (fim para terminar): ")
 if lista1 == "fim":
  break
 L.append(lista1)
while True:
 lista2 = input("Digite um valor para 2ª lista (fim para terminar): ")
 if lista2 == "fim":
  break
 V.append(lista2)
Z = []
Z.extend(L + V)
print(Z)