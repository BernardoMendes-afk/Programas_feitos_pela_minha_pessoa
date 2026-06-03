L = [15, 7, 27, 39]
pesquisa = int(input("Digite o valor a pesquisar na lista: "))
x = 0
while x < len(L):
 if L[x] == pesquisa:
  break
 x += 1
if x < len(L):
 print(f"{pesquisa} achado na posição {x}.")
else:
 print(f"{pesquisa} não encontrado.")