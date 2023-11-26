from tkinter import *
from tkinter import messagebox
import mysql.connector
from tela_cadastro import tela_cadastro
from tela_principal import tela_principal

root1 = Tk()
root1.title('Login')
root1.geometry('500x600')
root1.config(bg='#072a4d')
root1.resizable(width=False, height=True)


def verificar_senha():
    login = nome_entrada.get().lower().strip()
    senha = senha_entrada.get().strip()

    if nome_entrada.get() == "" and senha_entrada.get() == "":
        messagebox.showwarning('Campo vazio', 'Preencha todos os campos')
        return

    else:
        con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='root', password='Kamenriderv3')
        query = 'SELECT Senha FROM Users WHERE Login = %s'  # consulta banco de dados
        cursor = con.cursor()
        cursor.execute(query, (login,))
        senha_armazenada = cursor.fetchone()
        cursor.close()
        con.close()

        if senha_armazenada is not None:
            senha_armazenada = senha_armazenada[0]
            # Verificar se a senha_digitada corresponde à senha_armazenada
            if senha_armazenada == senha:
                messagebox.showinfo('Usuário cadastrado', 'Bem Vindo ao BookBox')
                root1.destroy()
                # mostrar janela bookbox
                tela_principal()
            else:
                messagebox.showinfo('Senha incorreta', 'Verifique senha')
        else:
            messagebox.showinfo('Erro', 'Usuário não cadastrado')

    nome_entrada.delete(0, END)
    senha_entrada.delete(0, END)


frame_1 = Frame(root1, width=700, height=80, bg='#072a4d', relief='flat')
frame_1.grid(row=0, column=0)
l1 = Label(frame_1, text='Faça o Login', font='Terminal 30 bold', bg='#072a4d', fg='yellow', width=30)
l1.place(height=80, width=500)

nome = Label(root1, width=10, height=2, text='Login:', font='Terminal 15 bold', bg='#072a4d', fg='yellow', relief='flat')
nome.place(x=20, y=120)
nome_entrada = Entry(root1, width=40, justify='left', relief='solid')
nome_entrada.place(x=50, y=180)

senha = Label(root1, width=10, height=2, text='Senha:', font='Terminal 15 bold', bg='#072a4d', fg='yellow', relief='flat')
senha.place(x=20, y=210)
senha_entrada = Entry(root1, width=40, justify='left', relief='solid', show='*')
senha_entrada.place(x=50, y=270)

btn_entrar = Button(root1, command=verificar_senha, width=8, height=1, text='Ok', font='Arial 10 bold', relief='raised',
                    fg='black', bg='orange')
btn_entrar.place(x=50, y=330)

aviso_cadastro = Label(root1, width=20, height=3, text='Não possui cadastro?', font='Terminal 15 bold', bg='#072a4d',
                       fg='yellow', relief='flat')
aviso_cadastro.place(x=30, y=370)

btn_cadastrar = Button(root1, command=tela_cadastro, width=8, height=1, text='Cadastrar', font='Arial 10 bold',
                       relief='raised', bg='orange')
btn_cadastrar.place(x=290, y=385)

root1.mainloop()
