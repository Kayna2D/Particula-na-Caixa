from funcoes import *
import tkinter as tk
from tkinter import ttk, messagebox

h = 6.626E-34
c = 3E8
h_ev = 4.136E-15
me = 9.11E-31
mp = 1.67E-27

def calculo():
    try:
        largura = float(entry_largura.get())
        ni = float(entry_ni.get())
        nf = float(entry_nf.get())
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a > b:
            messagebox.showerror("Erro", "O valor inicial deve ser menor ou igual ao valor final")
        massa = mp if var_massa.get() == "mp" else me

        resultados = []
        resultados.append(funcOndaInicial(largura, ni))
        resultados.append(funcOndaFinal(largura, nf))
        resultados.append(f'Energia no nível inicial: {Decimal(en(ni, massa, largura)):.3E} J')
        resultados.append(f'Energia no nível inicial: {Decimal(en_ev(ni, massa, largura)):.3E} eV')
        resultados.append(f'Energia no nível final: {Decimal(en(nf, massa, largura)):.3E} J')
        resultados.append(f'Energia no nível final: {Decimal(en_ev(nf, massa, largura)):.3E} eV')
        resultados.append(f'Energia do fóton: {Decimal(efoton(ni, nf, massa, largura)):.3E} eV')
        resultados.append(f'Comprimento do fóton: {Decimal(comprimento(efoton(ni, nf, massa, largura))):.3E} m')
        resultados.append(f'Frequência do fóton: {Decimal(frequencia(efoton(ni, nf, massa, largura))):.3E} Hz')
        resultados.append(f'Velocidade inicial do fóton: {Decimal(velocidade(ni, massa, largura)):.3E} m/s')
        resultados.append(f'Velocidade final do fóton: {Decimal(velocidade(nf, massa, largura)):.3E} m/s')
        resultados.append(f'Comprimento de onda de De Broglie inicial: {Decimal(deBroglie(massa, velocidade(ni, massa, largura))):.3E} m')
        resultados.append(f'Comprimento de onda de De Broglie final: {Decimal(deBroglie(massa, velocidade(nf, massa, largura))):.3E} m')
        resultados.append(f'Probabilidade no nível inicial: {probabilidade(a, b, ni, largura)*100:.2f} %')
        resultados.append(f'Probabilidade no nível final: {probabilidade(a, b, nf, largura)*100:.2f} %')

        messagebox.showinfo("Resultados", "\n".join(resultados))

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos")

root = tk.Tk()
root.title("Particula na Caixa")

tk.Label(root, text="Partícula na Caixa", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Label(root, text="Largura (m):").grid(row=1, column=0, padx=10, pady=5)
entry_largura = tk.Entry(root)
entry_largura.grid(row=1, column=1)

tk.Label(root, text="Nível inicial:").grid(row=2, column=0, padx=10, pady=5)
entry_ni = tk.Entry(root)
entry_ni.grid(row=2, column=1)

tk.Label(root, text="Nível final:").grid(row=3, column=0, padx=10, pady=5)
entry_nf = tk.Entry(root)
entry_nf.grid(row=3, column=1)

tk.Label(root, text="Probabilidade (a <= x <= b)").grid(row=4, column=0, padx=5, pady=2)

tk.Label(root, text="a:").grid(row=5, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=5, column=1)

tk.Label(root, text="b:").grid(row=6, column=0, padx=10, pady=5)    
entry_b = tk.Entry(root)
entry_b.grid(row=6, column=1)

var_massa = tk.StringVar(value="me")
tk.Label(root, text="Massa (m):").grid(row=7, column=0, padx=10, pady=5)
tk.Radiobutton(root, text="Massa do próton", variable=var_massa, value="mp").grid(row=7, column=1)
tk.Radiobutton(root, text="Massa do elétron", variable=var_massa, value="me").grid(row=8, column=1)

tk.Button(root, text="Calcular", command=calculo).grid(row=9, column=0, columnspan=2, padx=10, pady=10)
tk.Button(root, text="Gráficos", command=0).grid(row=9, column=1, columnspan=2, pady=10)
tk.Button(root, text="Simulação", command=0).grid(row=10, column=0, columnspan=2, pady=10)
tk.Button(root, text="Sobre", command=0).grid(row=10, column=1, columnspan=2, pady=10)


root.mainloop()