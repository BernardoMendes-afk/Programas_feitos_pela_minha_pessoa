import tkinter as tk
from tkinter import messagebox
import csv
import time

# import serial # Descomente quando usar a Pico Física

# Criação do arquivo de Banco de Dados
ARQUIVO_DADOS = "historico_producao.csv"
with open(ARQUIVO_DADOS, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Data_Hora", "Setup_Selagem", "Velocidade_Esteira", "Pecas", "Eficiencia", "Status"])


def enviar_configuracao():
    try:
        vel = float(entry_vel.get())
        comp = float(entry_comp.get())
        espaco = float(entry_espaco.get())
        selagem = float(entry_selagem.get())

        # Validação de Engenharia: A esteira não pode entregar mais rápido que a selagem
        tempo_esteira = (comp + espaco) / vel
        if tempo_esteira < selagem:
            messagebox.showwarning("Erro de Setup",
                                   f"Engavetamento! A esteira entrega a cada {tempo_esteira:.2f}s, mas a selagem demora {selagem}s. Reduza a velocidade ou aumente o espaçamento.")
            return

        comando = f"CONF:{vel},{comp},{espaco},{selagem}\n"

        # Quando tiver a placa física, enviaremos via Serial:
        # porta_serial.write(comando.encode())

        lbl_status.config(text=f"Setup Enviado: {comando.strip()}", fg="green")

        # Simula o salvamento de um log no Banco de Dados
        with open(ARQUIVO_DADOS, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([time.strftime("%Y-%m-%d %H:%M:%S"), selagem, vel, 0, "0%", "SETUP_OK"])

    except ValueError:
        messagebox.showerror("Erro", "Insira apenas números.")


# --- Interface Gráfica (Tkinter) ---
janela = tk.Tk()
janela.title("IHM - Projeto Fluxo")
janela.geometry("350x400")

tk.Label(janela, text="Configuração da Máquina", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(janela, text="Velocidade da Esteira (m/s):").pack()
entry_vel = tk.Entry(janela);
entry_vel.insert(0, "0.25");
entry_vel.pack()

tk.Label(janela, text="Comprimento do Produto (m):").pack()
entry_comp = tk.Entry(janela);
entry_comp.insert(0, "0.15");
entry_comp.pack()

tk.Label(janela, text="Espaçamento (m):").pack()
entry_espaco = tk.Entry(janela);
entry_espaco.insert(0, "0.10");
entry_espaco.pack()

tk.Label(janela, text="Tempo de Selagem (s):").pack()
entry_selagem = tk.Entry(janela);
entry_selagem.insert(0, "1.2");
entry_selagem.pack()

tk.Button(janela, text="Enviar Setup para Máquina", command=enviar_configuracao, bg="lightblue").pack(pady=20)
lbl_status = tk.Label(janela, text="Aguardando...", fg="gray")
lbl_status.pack()

janela.mainloop()