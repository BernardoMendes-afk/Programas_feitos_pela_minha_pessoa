casa = float(input("Indique o valor da casa: "))
salario = float(input("Indique seu salário: "))
anos = float(input("Indique a quantidade de anos a pagar: "))

prestacao = casa/anos
percentual = (salario/100)*30

if prestacao > percentual:
    print("O seu empréstimo foi aceito! Aproveite sua nova casa")

elif prestacao < percentual:
    print("Seu empréstimo não foi aprovado!")
