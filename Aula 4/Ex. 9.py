deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (ex: 3 para 3%): "))
dep_por_mes = float(input("Valor depositado mensalmente: "))
print("-" * 45)
mes = 1
saldo = deposito
total_investido = deposito

while mes <= 24:
    if mes > 1:
        saldo = saldo + dep_por_mes
        total_investido = total_investido + dep_por_mes
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Mês {mes}: R$ {saldo:.2f}")
    mes = mes + 1

print("-" * 45)
print(f"Total ganho com juros: R$ {saldo - total_investido:.2f}")