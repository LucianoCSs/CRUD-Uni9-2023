from tkinter import *
from tkinter import messagebox
import mysql.connector
import tkinter

global root2


def tela_cadastro():
    global root2
    global nome_c_entrada
    global novo_login_entrada
    global nova_senha_entrada
    root2 = tkinter.Toplevel()
    root2.title('Cadastro')
    root2.geometry('500x600')
    root2.config(bg='#072a4d')
    root2.resizable(width=False, height=True)

    frame_2 = Frame(root2, width=700, height=80, bg='#072a4d', relief='flat')
    frame_2.grid(row=0, column=0)
    l2 = Label(frame_2, text='Faça o Cadastro', font='Terminal 30 bold', bg='#072a4d', fg='yellow', width=30)
    l2.place(height=80, width=500)

    nome_c = Label(root2, width=20, height=2, text='Nome completo:', font='Terminal 15 bold', bg='#072a4d', fg='yellow', relief='flat')
    nome_c.place(x=5, y=120)
    nome_c_entrada = Entry(root2, width=40, justify='left', relief='solid')
    nome_c_entrada.place(x=50, y=180)

    novo_login = Label(root2, width=10, height=2, text='Login:', font='Terminal 15 bold', bg='#072a4d', fg='yellow', relief='flat')
    novo_login.place(x=20, y=210)
    novo_login_entrada = Entry(root2, width=40, justify='left', relief='solid')
    novo_login_entrada.place(x=50, y=270)

    nova_senha = Label(root2, width=10, height=2, text='Senha:', font='Terminal 15 bold', bg='#072a4d', fg='yellow', relief='flat')
    nova_senha.place(x=20, y=310)
    nova_senha_entrada = Entry(root2, width=40, justify='left', relief='solid', show='*')
    nova_senha_entrada.place(x=50, y=370)

    btn_novo_cadastro = Button(root2, command=cadastrar, width=8, height=1, text='Ok', font='Arial 10 bold', relief='raised', bg='orange')
    btn_novo_cadastro.place(x=50, y=430)


def cadastrar():
    nc = nome_c_entrada.get().strip().title()
    nl = novo_login_entrada.get().strip().lower()
    ns = nova_senha_entrada.get().strip()

    if nome_c_entrada.get() == "" and novo_login_entrada.get() == "" and nova_senha_entrada.get() == "":
        messagebox.showwarning('Campo vazio', 'Preencha todos os campos')
        return

    else:
        con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='root', password='Kamenriderv3')
        dados = f'INSERT INTO Users (Nome, Login, Senha) VALUES ("{nc}", "{nl}", "{ns}")'
        cursor = con.cursor()
        cursor.execute(dados)
        con.commit()  # edita banco de dados
        cursor.close()
        con.close()
        nome_c_entrada.delete(0, END)
        novo_login_entrada.delete(0, END)
        nova_senha_entrada.delete(0, END)
        messagebox.showinfo('Novo Usuário', 'Nova conta criada com sucesso!')
        root2.destroy()




