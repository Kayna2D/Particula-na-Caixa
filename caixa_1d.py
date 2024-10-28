import tkinter as tk
from tkinter import ttk, messagebox

def calcular():
    # Implemente a lógica para mostrar os seguintes resultados na janela:
    # Largura da caixa
    # Nível quântico da partícula
    # Probabilidade de encontrar a partícula na posição x
    # Dica: dá uma olhada na função cálculo em main.py
    return 0

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