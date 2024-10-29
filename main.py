from funcoes import *
from caixa_1d  import *
import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
from matplotlib.animation import FuncAnimation

h = 6.626E-34
c = 3E8
h_ev = 4.136E-15
me = 9.11E-31
mp = 1.67E-27 
retorno = False 

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

def plotar():
    try:
        l = float(entry_largura.get())
        ni = float(entry_ni.get())
        nf = float(entry_nf.get())
        
        x_vals = np.linspace(0, l, 500)

        fo_ni = funcaoOndaGraf(l, ni)
        fo_nf = funcaoOndaGraf(l, nf)

        prob_ni = probabilidadeGraf(ni, l)
        prob_nf = probabilidadeGraf(nf, l)

        fig, axs = plt.subplots(2, 2, figsize=(10, 6))

        axs[0, 0].plot(x_vals, fo_ni(x_vals))
        axs[0, 0].set_title(f'Função de onda (n={int(ni)})')
        axs[0, 0].set_xlabel('x (m)')
        axs[0, 0].set_ylabel('Ψ')

        axs[0, 1].plot(x_vals, fo_nf(x_vals))
        axs[0, 1].set_title(f'Função de onda (n={int(nf)})')
        axs[0, 1].set_xlabel('x (m)')
        axs[0, 1].set_ylabel('Ψ')

        axs[1, 0].plot(x_vals, prob_ni(x_vals))
        axs[1, 0].set_title(f'Distribução de Probabilidade (n={int(ni)})')
        axs[1, 0].set_xlabel('x (m)')
        axs[1, 0].set_ylabel('|Ψ|²')

        axs[1, 1].plot(x_vals, prob_nf(x_vals))
        axs[1, 1].set_title(f'Distribução de Probabilidade (n={int(nf)})')
        axs[1, 1].set_xlabel('x (m)')
        axs[1, 1].set_ylabel('$Ψ|²')

        plt.tight_layout()
        plt.show()

    except ValueError:
        messagebox.showerror("Erro", "Por favor, insira valores válidos")

def simular():
    niveis_energia = np.array([1, 2, 3, 4, 5])
    velocidades = {1: 0.05, 2: 0.1, 3: 0.15, 4: 0.2, 5: 0.25}
    estado_atual = 1
    estados = [estado_atual]
    estado_final = np.random.randint(2, 6)
    estados.append(estado_final)

    while estado_final != 1:
        proximo_salto = np.random.randint(1, estado_final)
        estados.append(proximo_salto)
        estado_final = proximo_salto

    fig, ax = plt.subplots()
    ax.set_xlim(0, 2)
    ax.set_ylim(0, 6)
    ax.set_xticks([])
    ax.set_yticks(niveis_energia)
    ax.set_yticklabels([f'{-13.6/n**2:.2f} E{int(n)}' for n in niveis_energia])
    ax.set_title("Simulação de Saltos Quânticos")

    for nivel in niveis_energia:
        ax.hlines(nivel, xmin=0, xmax=2, colors="gray", linestyles="dotted")

    particula, = ax.plot(0.5, 1, 'ro', markersize=10)
    foton_absorvido, = ax.plot([], [], 'bo', markersize=5)  
    foton_emitido, = ax.plot([], [], 'bo', markersize=5)

    frames_por_salto = 60
    total_frames = (len(estados) - 1) * frames_por_salto
    

    def atualizar(frame):
        
        i = frame // frames_por_salto
        progresso = (frame % frames_por_salto) / frames_por_salto

        if i < len(estados) - 1:
            nivel_inicial = estados[i]
            nivel_final = estados[i + 1]

            x_pos = 1 + 0.5 * np.sin(velocidades[nivel_inicial] * frame)
            particula.set_xdata(x_pos)
            particula.set_ydata(nivel_final if progresso == 0 else nivel_inicial)

            if nivel_final > nivel_inicial:  
                    if progresso == 0:
                        foton_absorvido.set_data(0.2, nivel_inicial)
                        foton_emitido.set_data([], [])
                    elif progresso < 1.0:
                        foton_x = 0.2 + (x_pos - 0.2) * progresso
                        foton_absorvido.set_data(foton_x, nivel_inicial)
                        foton_emitido.set_data([], [])
                    else:
                        foton_absorvido.set_data([], [])
            
            elif nivel_final < nivel_inicial:  
                foton_absorvido.set_data([], [])
                if i > 0:
                    nivel_anterior = estados[i]
                    if progresso < 0.7:
                        foton_emitido.set_data([], [])
                    elif progresso < 1.0:
                        progresso_foton = (progresso - 0.7) / 0.3
                        foton_x = 1.5 + 0.5 * progresso_foton
                        foton_emitido.set_data(foton_x, nivel_anterior)  
                    else:
                        foton_emitido.set_data([], [])
                else: 
                    foton_emitido.set_data([], [])    
        
        return particula, foton_absorvido, foton_emitido

    anim = FuncAnimation(fig, atualizar, frames=total_frames, interval=20, blit=True)
    
    plt.show()

def sobre():
    texto_sobre = (
        "Partícula na Caixa\n\n"
        "Autores: Kaynã de Deus / Mario Eugenio\n"
        "Linguagem: Python\n\n"
        "Bibliotecas:\n"
        "math e numpy: Funções matemáticas\n"
        "decimal: Formatação de números\n"
        "scipy: Cálculo das integrais\n"
        "tkinter: Interface gráfica\n"
        "matplotlib: Desenvolvimento dos gráficos e simulação\n\n"
        "Este programa permite que você explore propriedades quânticas de uma partícula confinada "
        "em uma 'caixa de potencial'. Ele possui funcionalidades para cálculos de energia, funções de onda, "
        "gráficos de probabilidade e uma simulação de saltos quânticos entre níveis de energia."
    )
    messagebox.showinfo("Sobre o Programa", texto_sobre)

root = tk.Tk()
root.title("Particula na Caixa")

tk.Label(root, text="Partícula na Caixa", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

tk.Button(root, text="Caixa 1D", command=lambda: caixa_1d(root)).grid(row=11, column=0, columnspan=2, pady=10)

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
tk.Button(root, text="Gráficos", command=plotar).grid(row=9, column=1, columnspan=2, pady=10)
tk.Button(root, text="Simulação", command=simular).grid(row=10, column=0, columnspan=2, pady=20)
tk.Button(root, text="Sobre", command=sobre).grid(row=10, column=1, columnspan=2, pady=10)


root.mainloop()