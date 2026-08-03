A = []
B = []
while True:
 lista1 = input("Digite um valor para 1ª lista (fim para terminar): ")
 if lista1 == "fim":
  break
 A.append(lista1)
while True:
 lista2 = input("Digite um valor para 2ª lista (fim para terminar): ")
 if lista2 == "fim":
  break
 B.append(lista2)
C = []
C.extend(A + B)
print(C)
C.sort()
print(C)