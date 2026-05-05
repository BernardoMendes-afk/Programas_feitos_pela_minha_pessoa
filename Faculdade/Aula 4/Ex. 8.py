deposito = float(input("Depósito inicial: "))
taxa = float(input("Taxa de juros (o valor sairá em porcentagem): "))
print("-"*45)
mes = 1
saldo = deposito

while mes <= 24:
    saldo = saldo + (saldo * (taxa / 100))
    print(f"Mês {mes}: R$ {saldo:.2f}")
    mes = mes + 1

print("-" * 45)
print(f"Total ganho com juros: R$ {saldo - deposito:.2f}")