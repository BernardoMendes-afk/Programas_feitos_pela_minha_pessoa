a = 2
b = 3

soma = a+b
subtracao = a-b
multiplicacao = a*b
divisao = a/b

print("1. Soma")
print("2. Subtracao")
print("3. Multiplicacao")
print("4. Divisao")
print("-" * 30)
opcao = int(input("Qual operação deseja realizar?: "))

if opcao == 1:
    print("-" * 30)
    print(soma)
elif opcao == 2:
    print("-" * 30)
    print(subtracao)
elif opcao == 3:
    print("-" * 30)
    print(multiplicacao)
elif opcao == 4:
    print("-" * 30)
    print(divisao)
else:
    print("-" * 30)
    print("Seu animal")
