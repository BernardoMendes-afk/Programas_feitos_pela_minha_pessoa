#Link do vídeo explicativo: [Insira aqui o link do seu vídeo do YouTube ou Drive de até 3 minutos]
#Integrantes: Bernardo Romeira Mendes - RM: 573355 & Isabel Ayumi Watanabe - RM: 569599

print("="*81)
print("SISTEMA DE MONITORAMENTO DE MÓDULOS ESPACIAIS - CONTROLE DE TERRA (CÁPSULA ÓREON)")
print("="*81)

#Inicialização manual das variáveis de controle e estatística
total_leituras = 0

#Acumuladores (somas para cálculo de média)
soma_vibracao = 0.0
soma_temperatura = 0.0
soma_latencia = 0
soma_cpu = 0

#Inicialização de máximos e mínimos
#Iniciamos os máximos com valores muito baixos e os mínimos com valores muito altos
max_vibracao = -9999.0
min_vibracao = 9999.0

max_temperatura = -9999.0
min_temperatura = 9999.0

max_latencia = -9999
min_latencia = 9999

max_cpu = -9999
min_cpu = 9999

#Estrutura de repetição (loop de telemetria)
while True:
    print()
    print("-"*75)
    opcao = input("Deseja inserir uma nova leitura de telemetria? (S para Sim / N para Sair): ")

    #Validação para encerrar o programa
    if opcao == "N" or opcao == "n":
        print("Encerrando a coleta de dados e gerando relatório final...")
        break
    elif opcao != "S" and opcao != "s":
        print("Opção inválida! Digite apenas S ou N.")
        continue  # Volta para o início do loop pedir a opção correta

    print("\nInsira os dados de sinal dos sensores")

    #1.Entrada e conversão de dados
    vibracao = float(input("Vibração estrutural da fuselagem (em G): "))
    temperatura = float(input("Temperatura dos painéis solares (em °C): "))
    latencia = int(input("Latência de comunicação com a Terra (em ms): "))
    uso_cpu = int(input("Uso de processamento da CPU de bordo (em %): "))

    #Análise crítica dos níveis elétricos/operacionais
    #Alertas automáticos imediatos baseados em limites de tolerância física
    if vibracao > 4.5:
        print("[ALERTA CRÍTICO]: Vibração intensa detectada! Risco de fadiga de material.")
    elif vibracao < 0.2:
        print("[ALERTA]: Baixa vibração ou ausência de aceleração.")

    if temperatura > 35.0:
        print("[ALERTA CRÍTICO]: Superaquecimento nos painéis! Ativar dissipadores de emergência.")
    elif temperatura < -10.0:
        print("[ALERTA CRÍTICO]: Congelamento detectado! Ligar aquecedores internos.")

    if latencia > 500:
        print("[ALERTA]: Latência de rede muito alta. Possível perda de pacotes com a Terra.")

    if uso_cpu > 90:
        print("[ALERTA CRÍTICO]: Sobrecarga no processador de bordo! Abortar processos secundários.")

    #Processamento dos extremos (máximo e mínimo manual)
    #Lógica estruturada apenas com if

    #Extremos de Vibração
    if vibracao > max_vibracao:
        max_vibracao = vibracao
    if vibracao < min_vibracao:
        min_vibracao = vibracao

    #Extremos de Temperatura
    if temperatura > max_temperatura:
        max_temperatura = temperatura
    if temperatura < min_temperatura:
        min_temperatura = temperatura

    #Extremos de Latência
    if latencia > max_latencia:
        max_latencia = latencia
    if latencia < min_latencia:
        min_latencia = latencia

    #Extremos de CPU
    if uso_cpu > max_cpu:
        max_cpu = uso_cpu
    if uso_cpu < min_cpu:
        min_cpu = uso_cpu

    #Atualização dos contadores e acumuladores
    total_leituras += 1
    soma_vibracao += vibracao
    soma_temperatura += temperatura
    soma_latencia += latencia
    soma_cpu += uso_cpu

    print("[INFO]: Dados computados com sucesso")

#Exibição do relatório(fora do loop while)
#Proteção lógica para evitar divisão por zero caso o usuário saia logo no início
if total_leituras > 0:
    #2.Cálculo correto de estatísticas
    media_vibracao = soma_vibracao / total_leituras
    media_temperatura = soma_temperatura / total_leituras
    media_latencia = soma_latencia / total_leituras
    media_cpu = soma_cpu / total_leituras

    print("\n" + "=" * 58)
    print("RELATÓRIO CONSOLIDADO DE TELEMETRIA ESPACIAL - CÁPSULA ÓREON")
    print("=" * 58)
    print(f"Total de registros analisados pela CPU de Terra: {total_leituras}")
    print("-" * 67)

    #Exibição dos resultados com formatação decimal utilizando f-strings
    print(f"VIBRAÇÃO ESTRUTURAL (G):")
    print(f"  > Média Período: {media_vibracao:.2f} G")
    print(f"  > Pico Máximo  : {max_vibracao:.2f} G")
    print(f"  > Ponto Mínimo : {min_vibracao:.2f} G")
    print("-" * 67)

    print(f"TEMPERATURA OPERACIONAL (°C):")
    print(f"  > Média Período: {media_temperatura:.1f} °C")
    print(f"  > Pico Máximo  : {max_temperatura:.1f} °C")
    print(f"  > Ponto Mínimo : {min_temperatura:.1f} °C")
    print("-" * 67)

    print(f"LATÊNCIA DE REDE (ms):")
    print(f"  > Média Período: {media_latencia:.1f} ms")
    print(f"  > Pico Máximo  : {max_latencia} ms")
    print(f"  > Ponto Mínimo : {min_latencia} ms")
    print("-" * 67)

    print(f"USO DE PROCESSAMENTO CPU (%):")
    print(f"  > Média Período: {media_cpu:.1f} %")
    print(f"  > Pico Máximo  : {max_cpu} %")
    print(f"  > Ponto Mínimo : {min_cpu} %")
    print("=" * 58)
    print("FIM DO PROCESSAMENTO DE DADOS AVIÔNICOS - MISSÃO CONCLUÍDA")
    print("=" * 58)
else:
    print("\n[AVISO]: Nenhuma leitura válida foi inserida pelo terminal.")
    print("Nenhum dado estatístico foi gerado.")