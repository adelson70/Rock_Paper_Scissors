import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter.font import Font
from random import choice
import pandas as pd

objetos = ['pedra','papel','tesoura']

placar = {
    'rodada':[],
    'usuario':[],
    'computador':[],
    'resultado':[],
}

def maquina_escolher():
    global objetos
    maquina = choice(objetos)
    return maquina

def centralizar_tela():
    largura = 300
    altura = 390

    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    x = (largura_tela- largura) // 2
    y = (altura_tela- altura) // 2

    janela.geometry(f"{largura}x{altura}+{x}+{y}")

def salvar_partidas():
    global placar

    if len(placar['rodada']) == 0:
        return messagebox.showerror(f'Erro ao Salvar!',f'Você Não Jogou Nenhuma Partida Ainda!')


    arquivo = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Arquivos Excel", "*.xlsx"), ("Todos os arquivos", "*.*")])

    # Verifica se o usuário escolheu um arquivo
    if arquivo:
        df = pd.DataFrame(placar)

        # Obtém o nome do arquivo a partir do caminho completo
        nome = arquivo.split("/")[-1].split(".")[0]

        df.to_excel(arquivo, index=False)

        messagebox.showinfo('ARQUIVO SALVO', f'O arquivo {nome}.xlsx foi salvo com sucesso!')

    else:
        messagebox.showerror(f'ERRO AO SALVAR',f'Você não escolheu um local para salvar o arquivo!')

def jogar(escolha_usuario):
    global placar
    maquina = maquina_escolher()
    usuario = escolha_usuario
    name_user = str(nome_usuario.get())

    if len(name_user) == 0:
        return messagebox.showerror(f'Sem Nome',f'Você não digitou nenhum nome!')

    if maquina == 'pedra' and usuario == 'tesoura' or maquina == 'tesoura' and usuario == 'papel' or maquina == 'papel' and usuario == 'pedra':
        resultado = 'Computador'
        placar['resultado'].append(resultado)
        partida = len(placar['resultado'])
        placar['rodada'].append(partida)

    elif maquina == usuario:
        resultado = 'Empate'
        placar['resultado'].append(resultado)
        partida = len(placar['resultado'])
        placar['rodada'].append(partida)

    else:
        resultado = f'{name_user.capitalize()}'
        placar['resultado'].append(resultado)
        partida = len(placar['resultado'])
        placar['rodada'].append(partida)

    placar['computador'].append(maquina)
    placar['usuario'].append(usuario)

    resumo = f"""
{name_user.capitalize()}: {usuario.upper()}
Computador: {maquina.upper()}

Resultado foi {resultado}
""" if resultado == 'Empate' else f"""
{name_user.capitalize()}: {usuario.upper()}
Computador: {maquina.upper()}

{resultado} foi o Vencedor da Partida!
"""
    messagebox.showinfo(f'Resultado da Partida {partida}',f'{resumo}')


# Criando um objeto de nome janela
janela = tk.Tk()
janela.title('PEDRA PAPEL TESOURA')

# fonte personalizada aplicada aos botões e labels
fonte_personalizada = Font(family="Helvetica", size=11, weight="bold")

# Opção para o usuário escolher um nome de jogador
tk.Label(text='Digite seu nome',font=fonte_personalizada).pack(pady=10)
nome_usuario = tk.Entry(janela)
nome_usuario.pack(pady=10)

# Parte da janela onde tem os botões para o jogador escolher a sua opção
tk.Label(text='Escolha uma opção para jogar!',font=fonte_personalizada).pack(pady=10)

# Botões do jogo
botao_pedra = tk.Button(text='PEDRA',font=fonte_personalizada,command=lambda:jogar('pedra'), width=20)
botao_papel = tk.Button( text='PAPEL',font=fonte_personalizada,command=lambda:jogar('papel'), width=20)
botao_tesoura = tk.Button( text='TESOURA',font=fonte_personalizada,command=lambda:jogar('tesoura'), width=20)

# ajustando tamanho dos botões
botao_pedra.pack(pady=10)
botao_papel.pack(pady=10)
botao_tesoura.pack(pady=10)

# Botão de salvar as partidas numa planilha do excel
tk.Label(text="Caso deseje salvar as partidas",font=fonte_personalizada).pack(pady=10)
botao_salvar = tk.Button( text='SALVAR',font=fonte_personalizada,command=lambda:salvar_partidas(), width=20)
botao_salvar.pack(pady=10)

centralizar_tela()

janela.mainloop()