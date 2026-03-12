#Tempo

temp_dias = float(input("Digite o número de dias:"))
temp_horas = float(input("Digite o tempo em horas:"))
temp_minutos = float(input("Digite o tempo em minutos:"))
temp_segundos = float(input("Digite o tempo em segundos:"))

total_segundos = (temp_dias*86400)+(temp_horas*3600)+(temp_minutos*60)+temp_segundos

print("O tempo total, em segundos, é de",total_segundos)
