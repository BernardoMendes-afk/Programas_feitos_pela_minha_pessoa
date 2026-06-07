# Link do vídeo explicativo: 
# Integrantes: Bernardo Romeira Mendes - RM: 573355 & Isabel Ayumi Watanabe - RM: 569599

print("=======================================================")
print("SISTEMA DE MONITORAMENTO ESPACIAL - ORBITALTECH")
print("=======================================================")

# Pede quantos ciclos o usuário quer rodar (o mínimo são 3 ciclos):
num_ciclos = int(input("Quantos ciclos de leitura deseja realizar? "))
while num_ciclos < 3:
    print("Quantidade invalida! Digite no minimo 3 ciclos.")
    num_ciclos = int(input("Quantos ciclos de leitura deseja realizar? "))

# Contador de leituras dos sensores e acumuladores para as médias:
total_leituras_sensores = 0
leituras_criticas = 0

soma_vibracao = 0.0
soma_temperatura = 0.0
soma_latencia = 0
soma_cpu = 0

# Variável que acumula as mensagens de alerta para exibir no final:
alertas_finais = ""

# Loop para controlar os ciclos:
ciclo_atual = 1
while ciclo_atual <= num_ciclos:
    print("\n--- CONTROLE DO CICLO", ciclo_atual, "---")

    # Leitura da CPU Geral realizada uma única vez por ciclo (exigência da professora):
    uso_cpu = int(input("Digite o uso da CPU geral do modulo (em %): "))
    soma_cpu = soma_cpu + uso_cpu

    # Verifica o alerta de CPU e calcula máximo e mínimo dela por ciclo:
    if uso_cpu > 85:
        msg = "ALERTA: Uso de CPU critico de " + str(uso_cpu) + "% detectado no sistema geral (Ciclo " + str(
            ciclo_atual) + ")!"
        print("  [!] ", msg)
        alertas_finais = alertas_finais + msg + "\n"
        leituras_criticas = leituras_criticas + 1

    if ciclo_atual == 1:
        max_cpu = uso_cpu
        min_cpu = uso_cpu
    else:
        if uso_cpu > max_cpu:
            max_cpu = uso_cpu
        if uso_cpu < min_cpu:
            min_cpu = uso_cpu

    # Loop interno para passar pelos 5 pontos de sensores (S1 até S5):
    ponto_atual = 1
    while ponto_atual <= 5:
        print("  Sensor S" + str(ponto_atual) + ":")

        # Pede os dados específicos de cada ponto de sensor:
        vibracao = float(input("    Digite a vibracao (em g): "))
        temperatura = float(input("    Digite a temperatura (em C): "))
        latencia = int(input("    Digite a latencia (em ms): "))

        # Sinalizador para saber se este ponto teve algum problema:
        deu_erro_aqui = False

        # Testa se os valores dos sensores estão fora dos limites de segurança com mensagens detalhadas:
        if vibracao > 5.0 or vibracao < -5.0:
            msg = "ALERTA: Vibracao critica de " + str(vibracao) + "g detectada no ponto S" + str(
                ponto_atual) + " (Ciclo " + str(ciclo_atual) + ")!"
            print("    [!] ", msg)
            alertas_finais = alertas_finais + msg + "\n"
            deu_erro_aqui = True

        if temperatura > 120.0 or temperatura < -150.0:
            msg = "ALERTA: Temperatura critica de " + str(temperatura) + "C detectada no ponto S" + str(
                ponto_atual) + " (Ciclo " + str(ciclo_atual) + ")!"
            print("    [!] ", msg)
            alertas_finais = alertas_finais + msg + "\n"
            deu_erro_aqui = True

        if latencia > 800:
            msg = "ALERTA: Latencia critica de " + str(latencia) + "ms detectada no ponto S" + str(
                ponto_atual) + " (Ciclo " + str(ciclo_atual) + ")!"
            print("    [!] ", msg)
            alertas_finais = alertas_finais + msg + "\n"
            deu_erro_aqui = True

        # Se teve algum erro nas checagens do sensor acima, conta como leitura crítica de forma simples:
        if deu_erro_aqui == True:
            leituras_criticas = leituras_criticas + 1

        # Lógica para achar o maior e o menor valor de todos os sensores:
        if total_leituras_sensores == 0:
            max_vibracao = vibracao
            min_vibracao = vibracao
            max_temperatura = temperatura
            min_temperatura = temperatura
            max_latencia = latencia
            min_latencia = latencia
        else:
            if vibracao > max_vibracao:
                max_vibracao = vibracao
            if vibracao < min_vibracao:
                min_vibracao = vibracao

            if temperatura > max_temperatura:
                max_temperatura = temperatura
            if temperatura < min_temperatura:
                min_temperatura = temperatura

            if latencia > max_latencia:
                max_latencia = latencia
            if latencia < min_latencia:
                min_latencia = latencia

        # Soma os valores para calcular a média e conta mais uma leitura de sensor feita:
        soma_vibracao = soma_vibracao + vibracao
        soma_temperatura = soma_temperatura + temperatura
        soma_latencia = soma_latencia + latencia
        total_leituras_sensores = total_leituras_sensores + 1

        ponto_atual = ponto_atual + 1  # Avança do sensor S1 até chegar no S5

    ciclo_atual = ciclo_atual + 1  # Vai para o próximo ciclo de leitura

# Faz as contas finais das médias de cada parâmetro:
media_vibracao = round(soma_vibracao / total_leituras_sensores, 2)
media_temperatura = round(soma_temperatura / total_leituras_sensores, 2)
media_latencia = round(soma_latencia / total_leituras_sensores, 2)
media_cpu = round(soma_cpu / num_ciclos, 2)

# O total de checagens feitas pelo sistema inclui todas as leituras de sensores + leituras de CPU:
total_checagens_gerais = total_leituras_sensores + num_ciclos
porcentagem_critica = round((leituras_criticas / total_checagens_gerais) * 100, 2)

if porcentagem_critica > 30.0:
    estado_geral = "ESTADO GERAL: RISCO ELEVADO - Acionar protocolo de emergencia"
elif porcentagem_critica >= 10.0:
    estado_geral = "ESTADO GERAL: ATENCAO - Monitoramento intensificado recomendado"
else:
    estado_geral = "ESTADO GERAL: NORMAL - Modulo operando dentro dos limites de seguranca"

# Impressão do relatório final limpo, informativo e estruturado:
print("\n=======================================================")
print("=== RELATORIO FINAL DO PERIODO ===")
print("=======================================================")

print("1. LISTA DE ALERTAS CRITICOS DETECTADOS:")
if alertas_finais != "":
    print(alertas_finais)
else:
    print("Nenhum alerta critico foi gerado.")
print("-" * 55)

print("2. ESTATISTICAS DOS SENSORES (Media, Max, Min):")
print("Vibracao    -> Media:", media_vibracao, "g | Max:", max_vibracao, "g | Min:", min_vibracao, "g")
print("Temperatura -> Media:", media_temperatura, "C | Max:", max_temperatura, "C | Min:", min_temperatura, "C")
print("Latencia    -> Media:", media_latencia, "ms | Max:", max_latencia, "ms | Min:", min_latencia, "ms")
print("Uso de CPU  -> Media:", media_cpu, "% | Max:", max_cpu, "% | Min:", min_cpu, "%")
print("-" * 55)

print("3. CLASSIFICACAO DO ESTADO DO MODULO:")
print(estado_geral)
print("Porcentagem de situacoes criticas:", porcentagem_critica, "%")
print("=======================================================")