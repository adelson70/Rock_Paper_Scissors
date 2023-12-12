import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font


def centralizar_tela():
    largura = 300
    altura = 200

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela- largura) // 2
    y = (altura_tela- altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def jogar():
    ...



janela = tk.Tk()
fonte_personalizada = Font(family="Helvetica", size=11, weight="bold")


janela.title('PEDRA PAPEL TESOURA')
tk.Label(text='Escolha',font=fonte_personalizada).pack(pady=10)

# Botões do jogo
botao_pedra = tk.Button(text='PEDRA',font=fonte_personalizada,command=lambda:jogar(), width=20)
botao_papel = tk.Button( text='PAPEL',font=fonte_personalizada,command=lambda:jogar(), width=20)
botao_tesoura = tk.Button( text='TESOURA',font=fonte_personalizada,command=lambda:jogar(), width=20)

# ajustando tamanho dos botões
botao_pedra.pack(pady=10)
botao_papel.pack(pady=10)
botao_tesoura.pack(pady=10)

centralizar_tela()

janela.mainloop()