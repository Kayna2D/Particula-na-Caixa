from funcoes import *
import tkinter as tk
from tkinter import ttk, messagebox

h = 6.626E-34
c = 3E8
h_ev = 4.136E-15
me = 9.11E-31
mp = 1.67E-27

root = tk.Tk()
root.title("Particula na Caixa")

tk.Label(root, text="Largura (m):").grid(row=0, column=0, padx=10, pady=5)
entry_largura = tk.Entry(root)
entry_largura.grid(row=0, column=1)

tk.Label(root, text="Nível inicial:").grid(row=1, column=0, padx=10, pady=5)
entry_ni = tk.Entry(root)
entry_ni.grid(row=1, column=1)

tk.Label(root, text="Nível final:").grid(row=2, column=0, padx=10, pady=5)
entry_nf = tk.Entry(root)
entry_nf.grid(row=2, column=1)

tk.Label(root, text="Probabilidade (a <= x <= b)").grid(row=3, column=0, padx=5, pady=2)

tk.Label(root, text="a:").grid(row=4, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=4, column=1)

tk.Label(root, text="b:").grid(row=5, column=0, padx=10, pady=5)    
entry_b = tk.Entry(root)
entry_b.grid(row=5, column=1)

massa = tk.StringVar(value="me")
tk.Label(root, text="Massa (m):").grid(row=6, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Massa do próton", variable=massa, value="mp").grid(row=6, column=1)
tk.Radiobutton(root, text="Massa do elétron", variable=massa, value="me").grid(row=7, column=1)

tk.Button(root, text="Calcular", command=0).grid(row=8, column=0, columnspan=2, pady=10)
tk.Button(root, text="Gráficos", command=0).grid(row=8, column=1, columnspan=2, pady=10)
tk.Button(root, text="Simulação", command=0).grid(row=9, column=0, columnspan=2, pady=10)
tk.Button(root, text="Sobre", command=0).grid(row=9, column=1, columnspan=2, pady=10)


root.mainloop()