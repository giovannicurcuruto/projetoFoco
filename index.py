#Exemplo gerado inicialmente pelo CHAT GPT

import tkinter as tk
from tkinter import messagebox
import time


class FocusMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Monitor de Atividade")
        self.root.geometry("300x200")
        self.timer_running = False
        self.remaining_time = 0

        # Widgets
        self.label = tk.Label(self.root, text="Defina o tempo de foco (minutos):", font=("Arial", 12))
        self.label.pack(pady=10)

        self.time_entry = tk.Entry(self.root, font=("Arial", 14), justify="center")
        self.time_entry.pack(pady=5)

        self.start_button = tk.Button(self.root, text="Iniciar", font=("Arial", 12), command=self.start_timer)
        self.start_button.pack(pady=10)

        self.timer_label = tk.Label(self.root, text="", font=("Arial", 24), fg="green")
        self.timer_label.pack(pady=10)

    def start_timer(self):
        # Verifica se o timer já está rodando
        if self.timer_running:
            messagebox.showinfo("Atenção", "O timer já está em andamento.")
            return

        try:
            focus_time = int(self.time_entry.get()) * 60  # Converte minutos para segundos
            if focus_time <= 0:
                raise ValueError("Tempo inválido")
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número válido de minutos.")
            return

        self.remaining_time = focus_time
        self.timer_running = True
        self.update_timer()

    def update_timer(self):
        if self.remaining_time > 0:
            mins, secs = divmod(self.remaining_time, 60)
            self.timer_label.config(text=f"{mins:02}:{secs:02}")
            self.remaining_time -= 1
            self.root.after(1000, self.update_timer)  # Atualiza o timer a cada 1 segundo
        else:
            self.timer_running = False
            self.timer_label.config(text="Tempo esgotado!")
            messagebox.showinfo("Fim do tempo", "O tempo de foco terminou! Reprograme para continuar.")

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    app = FocusMonitor()
    app.run()
