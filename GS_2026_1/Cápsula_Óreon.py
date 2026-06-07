# Link do vídeo explicativo: 
# Integrantes: Bernardo Romeira Mendes - RM: 573355 & Isabel Ayumi Watanabe - RM: 569599

print("=======================================================")
print("SISTEMA DE MONITORAMENTO ESPACIAL - ORBITALTECH")
print("=======================================================")

num_ciclos = int(input("Quantos ciclos de leitura deseja realizar? "))
while num_ciclos < 3:
    print("Quantidade invalida! Digite no minimo 3 ciclos.")
    num_ciclos = int(input("Quantos ciclos de leitura deseja realizar? "))

total_leituras_sensores = 0
leituras_criticas = 0

soma_vibracao = 0.0
soma_temperatura = 0.0
soma_latencia = 0
soma_cpu = 0

alertas_finais = ""

ciclo_atual = 1
while ciclo_atual <= num_ciclos:
    print("\n--- CONTROLE DO CICLO", ciclo_atual, "---")

    uso_cpu = int(input("Digite o uso da CPU geral do modulo (em %): "))
    soma_cpu = soma_cpu + uso_cpu

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

    ponto_atual = 1
    while ponto_atual <= 5:
        print("  Sensor S" + str(ponto_atual) + ":")

        vibracao = float(input("    Digite a vibracao (em g): "))
        temperatura = float(input("    Digite a temperatura (em C): "))
        latencia = int(input("    Digite a latencia (em ms): "))

        if vibracao > 5.0 or vibracao < -5.0:
            msg = "ALERTA: Vibracao critica de " + str(vibracao) + "g detectada no ponto S" + str(
                ponto_atual) + " (Ciclo " + str(ciclo_atual) + ")!"
            print("    [!] ", msg)
            alertas_finais = alertas_finais + msg + "\n"
            leituras_criticas = leituras_criticas + 1

        if temperatura > 120.0 or temperatura < -150.0:
            msg = "ALERTA: Temperatura critica de " + str(temperatura) + "C detectada no ponto S" + str(
                ponto_atual) + " (Ciclo " + str(ciclo_atual) + ")!"
            print("    [!] ", msg)
            alertas_finais = alertas_finais + msg + "\n"
            leituras_criticas = leituras_criticas + 1

        if latencia > 800:
            msg = "ALERTA: Latencia critica de " + str(latencia) + "ms detectada no ponto S" + str(
                ponto_atual) + " (Ciclo " + str(ciclo_atual) + ")!"
            print("    [!] ", msg)
            alertas_finais = alertas_finais + msg + "\n"
            leituras_criticas = leituras_criticas + 1

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

        soma_vibracao = soma_vibracao + vibracao
        soma_temperatura = soma_temperatura + temperatura
        soma_latencia = soma_latencia + latencia
        total_leituras_sensores = total_leituras_sensores + 1

        ponto_atual = ponto_atual + 1

    ciclo_atual = ciclo_atual + 1

media_vibracao = round(soma_vibracao / total_leituras_sensores, 2)
media_temperatura = round(soma_temperatura / total_leituras_sensores, 2)
media_latencia = round(soma_latencia / total_leituras_sensores, 2)
media_cpu = round(soma_cpu / num_ciclos, 2)

# Considera todas as checagens realizadas (Sensores + CPU):
total_checagens_gerais = total_leituras_sensores + num_ciclos
porcentagem_critica = round((leituras_criticas / total_checagens_gerais) * 100, 2)

if porcentagem_critica > 30.0:
    estado_geral = "ESTADO GERAL: RISCO ELEVADO - Acionar protocolo de emergencia"
elif porcentagem_critica >= 10.0:
    estado_geral = "ESTADO GERAL: ATENCAO - Monitoramento intensificado recomendado"
else:
    estado_geral = "ESTADO GERAL: NORMAL - Modulo operando dentro dos limites de seguranca"

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