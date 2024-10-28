import tkinter as tk
from tkinter import messagebox
import numpy as np

def calcular():
    try:
        A = float(entry_a.get())
        k = float(entry_k.get())
        x = float(entry_x.get())

        # Calcular a função de onda
        psi_x = A * np.sin(k * x)
        
        # Calcular a probabilidade
        probabilidade = abs(psi_x) ** 2

        # Mostrar resultados
        resultados = (
            f'Função de onda (Ψ) em x={x:.4f} m: {psi_x:.4E}\n'
            f'Probabilidade de encontrar a partícula em x={x:.4f} m: {probabilidade:.4E} (em unidades de m⁻¹)'
        )
        messagebox.showinfo("Resultados da Caixa 1D", resultados)

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

    var_massa = tk.StringVar(value="me")
    tk.Label(caixa_1d_window, text="Partícula:").grid(row=2, column=0, padx=10, pady=5)
    tk.Radiobutton(caixa_1d_window, text="Próton", variable=var_massa, value="mp").grid(row=2, column=1, sticky="w")
    tk.Radiobutton(caixa_1d_window, text="Elétron", variable=var_massa, value="me").grid(row=3, column=1, sticky="w")
    
    tk.Label(caixa_1d_window, text="A (m):").grid(row=4, column=0, padx=10, pady=5)
    entry_a = tk.Entry(caixa_1d_window)
    entry_a.grid(row=4, column=1)

    tk.Label(caixa_1d_window, text="k (m):").grid(row=5, column=0, padx=10, pady=5)
    entry_k = tk.Entry(caixa_1d_window)
    entry_k.grid(row=5, column=1)

    tk.Label(caixa_1d_window, text="Posição de x:").grid(row=6, column=0, padx=10, pady=5)
    entry_x = tk.Entry(caixa_1d_window)
    entry_x.grid(row=6, column=1)

    tk.Button(caixa_1d_window, text="Calcular", command=calcular).grid(row=7, column=0, columnspan=2, pady=10)

# O resto do seu código principal deve estar aqui
