import tkinter as tk
from tkinter import messagebox
from funcoes import *
from decimal import Decimal

def calcular(entry_a, entry_k, entry_x):
    try:

        A = float(entry_a.get())
        k = float(entry_k.get())
        x = float(entry_x.get())

        resultados = []
        resultados.append(f'Largura: {Decimal(largura(A)):.3E}\n')
        resultados.append(f'Nível: {int(Decimal(nivel(largura(A), k)))}\n')
        resultados.append(f'Probabilidade de encontrar a partícula em x: {Decimal(prob_1d(largura(A), nivel(largura(A), k), x)):.3E} dx\n')
        
        messagebox.showinfo("Resultados da Caixa 1D", "\n".join(resultados))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos")

def caixa_1d(root):
    caixa_1d_window = tk.Toplevel(root)
    caixa_1d_window.title("Caixa 1D")

    tk.Label(caixa_1d_window, text="Caixa 1D", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    descricao = (
        "A função de onda (no SI) de uma partícula confinada em um poço de potencial infinito unidimensional é dada por:\n"
        "𝜓(𝑥) = 𝐴 sin(𝑘 ∙ 𝑥)"
    )
    tk.Label(caixa_1d_window, text=descricao, justify="left", wraplength=300).grid(row=1, column=0, columnspan=2, padx=10, pady=5)

    
    tk.Label(caixa_1d_window, text="A (m):").grid(row=2, column=0, padx=10, pady=5)
    entry_a = tk.Entry(caixa_1d_window)
    entry_a.grid(row=2, column=1)

    tk.Label(caixa_1d_window, text="k (m):").grid(row=3, column=0, padx=10, pady=5)
    entry_k = tk.Entry(caixa_1d_window)
    entry_k.grid(row=3, column=1)

    tk.Label(caixa_1d_window, text="Posição de x:").grid(row=4, column=0, padx=10, pady=5)
    entry_x = tk.Entry(caixa_1d_window)
    entry_x.grid(row=4, column=1)

    tk.Button(caixa_1d_window, text="Calcular", command=lambda:calcular(entry_a, entry_k, entry_x)).grid(row=5, column=0, columnspan=2, pady=10)

