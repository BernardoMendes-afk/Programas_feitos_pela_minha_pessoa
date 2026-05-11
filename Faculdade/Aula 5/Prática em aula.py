continuar = "s"
while continuar == "s":
    notas_cp = []
    soma = 0
    x = 0
    alun = int(input("Quantidade de alunos: "))
    while alun != len(notas_cp):
      nota = float(input(f"Checkpoint dos alunos {x+1} = "))
      if nota > 10:
           print("Inválida")
           break
      notas_cp.append(nota)
      soma += notas_cp[x]
      x += 1
    print(f"Média = {(soma/len(notas_cp)):.2f}")
    print(f"As notas digitadas foram: {notas_cp}")
    notas_cp.sort()
    print(f"As notas, em ordem crescente, são: {notas_cp}")
    notas_cp.sort(reverse=True)
    print(f"As notas, em ordem decrescente, são: {notas_cp}")
    print(f"A menor nota é: {min(notas_cp)}")
    print(f"A maior nota é: {max(notas_cp)}")
    notas_cp.clear()
    print(notas_cp)

#notas_checkpoints=[5,8,4,10]
#soma=0
#x=0
#while x<len(notas_checkpoints):
#soma = soma+notas_checkpoints[x]
#x=x+1
#print(f"A soma é de {soma} e média é de {(soma/len(notas_checkpoints))}")


#compras=["feijao","arroz","leite","biscoito"]
#print(compras)
#print(compras[0])
#compras[3]="bolacha"
#print(compras)