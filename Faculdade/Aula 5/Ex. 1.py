notas = [0, 0, 0, 0, 0, 0, 0]
soma = 0
x = 0
while x < 7:
 notas[x] = int(input(f"Nota {x+1} = "))
 soma += notas[x]
 x += 1
print(f"Média = {(soma/x):.2f}")