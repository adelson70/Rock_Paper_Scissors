import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
from random import choice
import pandas as pd

placar = {
    'rodada':[],
    'vencedor':[],
}

objetos = ['pedra','papel','tesoura']

def maquina_escolher():
    global objetos
    maquina = choice(objetos)
    return maquina

def centralizar_tela():
    largura = 300
    altura = 300

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela- largura) // 2
    y = (altura_tela- altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def jogar(escolha_usuario):
    maquina = maquina_escolher()
    usuario = escolha_usuario
    name_user = str(nome_usuario.get())

    if len(name_user) == 0:
        return messagebox.showerror(f'Sem Nome',f'Você não digitou nenhum nome!')

    if maquina == 'pedra' and usuario == 'tesoura' or maquina == 'tesoura' and usuario == 'papel' or maquina == 'papel' and usuario == 'pedra':
        resultado = 'Computador'

    elif maquina == usuario:
        resultado = 'Empate'

    else:
        resultado = f'{name_user.capitalize()}'

    resumo = f"""
{name_user.capitalize()}: {usuario.upper()}
Computador: {maquina.upper()}

Resultado foi {resultado}
""" if resultado == 'Empate' else f"""
{name_user.capitalize()}: {usuario.upper()}
Computador: {maquina.upper()}

{resultado} foi o Vencedor da Partida!
"""
    messagebox.showinfo(f'Resultado da Partida',f'{resumo}')



janela = tk.Tk()
fonte_personalizada = Font(family="Helvetica", size=11, weight="bold")


janela.title('PEDRA PAPEL TESOURA')

# usuario escolhe um nome
tk.Label(text='Digite seu nome',font=fonte_personalizada).pack(pady=10)
nome_usuario = tk.Entry(janela)
nome_usuario.pack(pady=10)

# parte do jogo
tk.Label(text='Escolha uma opção para jogar!',font=fonte_personalizada).pack(pady=10)

# Botões do jogo
botao_pedra = tk.Button(text='PEDRA',font=fonte_personalizada,command=lambda:jogar('pedra'), width=20)
botao_papel = tk.Button( text='PAPEL',font=fonte_personalizada,command=lambda:jogar('papel'), width=20)
botao_tesoura = tk.Button( text='TESOURA',font=fonte_personalizada,command=lambda:jogar('tesoura'), width=20)

# ajustando tamanho dos botões
botao_pedra.pack(pady=10)
botao_papel.pack(pady=10)
botao_tesoura.pack(pady=10)

centralizar_tela()

janela.mainloop()