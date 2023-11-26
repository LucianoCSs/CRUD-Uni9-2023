import tkinter
from tkinter import *
from tkinter import ttk
import mysql.connector
import base64
from PIL import Image, ImageTk
import io
from tkinter import messagebox
from mysql.connector import Error
from tkinter.filedialog import askopenfilename

global img


def tela_principal():
    root = Tk()
    root.title('Read')
    root.geometry('1600x850')
    root.config(bg='yellow')
    root.resizable(width=True, height=True)

    # Cadastro
    frame1 = Frame(root, width=450, height=780, bg='#072a4d')
    frame1.place(x=10, y=20)
    l1 = Label(frame1, width=10, height=2, anchor=NW, text='Cadastro', font='Terminal 30 bold', relief='flat',
               bg='#072a4d',
               fg='yellow')
    l1.place(x=10, y=20)

    titulo = Label(frame1, width=10, height=2, anchor=NW, text='Título:', font='Terminal 20 bold', relief='flat',
                   bg='#072a4d', fg='yellow')
    titulo.place(x=10, y=90)
    titulo_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    titulo_entrada.place(x=15, y=130)

    author = Label(frame1, width=20, height=2, anchor=NW, text='Autor:', font='Terminal 20 bold', relief='flat',
                   bg='#072a4d', fg='yellow')
    author.place(x=10, y=170)
    author_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    author_entrada.place(x=15, y=210)

    ISBN = Label(frame1, width=20, height=2, anchor=NW, text='ISBN:', font='Terminal 20 bold', relief='flat',
                 bg='#072a4d',
                 fg='yellow')
    ISBN.place(x=10, y=250)
    isbn_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    isbn_entrada.place(x=15, y=290)

    publishing = Label(frame1, width=20, height=2, anchor=NW, text='Editora:', font='Terminal 20 bold', relief='flat',
                       bg='#072a4d', fg='yellow')
    publishing.place(x=10, y=330)
    publishing_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    publishing_entrada.place(x=15, y=370)

    year = Label(frame1, width=20, height=2, anchor=NW, text='Ano:', font='Terminal 20 bold', relief='flat',
                 bg='#072a4d',
                 fg='yellow')
    year.place(x=10, y=410)
    year_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    year_entrada.place(x=15, y=450)

    genre = Label(frame1, width=20, height=2, anchor=NW, text='Gênero:', font='Terminal 20 bold', relief='flat',
                  bg='#072a4d', fg='yellow')
    genre.place(x=10, y=490)
    genre_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    genre_entrada.place(x=15, y=530)

    pages = Label(frame1, width=20, height=2, anchor=NW, text='Páginas:', font='Terminal 20 bold', relief='flat',
                  bg='#072a4d', fg='yellow')
    pages.place(x=10, y=570)
    pages_entrada = Entry(frame1, width=60, justify='left', relief='solid')
    pages_entrada.place(x=15, y=610)

    # Pesquisa
    frame2 = Frame(root, width=1050, height=240, bg='#072a4d')
    frame2.place(x=480, y=20)
    l2 = Label(frame2, width=15, height=2, anchor=NW, text='Pesquisar por:', font='Terminal 20 bold', relief='flat',
               bg='#072a4d', fg='yellow')
    l2.place(x=10, y=30)
    combo = ttk.Combobox(frame2, width=15, height=10)
    combo['values'] = ('Título', 'Autor', 'Editora', 'Gênero', 'ISBN')
    combo.current()
    combo.place(x=290, y=35)
    search_entrada = Entry(frame2, relief='solid', width=30)
    search_entrada.place(x=420, y=35)

    # Visualização
    view = Label(frame2, width=25, height=2, text='ID do Livro:', font='Terminal 20 bold', relief='flat',
                 bg='#072a4d', fg='yellow', anchor=NW)
    view.place(x=10, y=120)
    view_entrada = Entry(frame2, width=10, relief='solid', justify='left')
    view_entrada.place(x=240, y=125)

    # tabela
    tv = ttk.Treeview(root, height=25, columns=('ID', 'Título', 'Autor', 'ISBN', 'Editora', 'Ano', 'Gênero', 'Páginas'),
                      show='headings')
    tv.column('ID', minwidth=0, width=80)
    tv.column('Título', minwidth=0, width=200)
    tv.column('Autor', minwidth=0, width=200)
    tv.column('ISBN', minwidth=0, width=150)
    tv.column('Editora', minwidth=0, width=150)
    tv.column('Ano', minwidth=0, width=50)
    tv.column('Gênero', minwidth=0, width=150)
    tv.column('Páginas', minwidth=0, width=70)
    tv.heading('ID', text='ID')
    tv.heading('Título', text='TITULO')
    tv.heading('Autor', text='AUTOR')
    tv.heading('ISBN', text='ISBN')
    tv.heading('Editora', text='EDITORA')
    tv.heading('Ano', text='ANO')
    tv.heading('Gênero', text='GENERO')
    tv.heading('Páginas', text='PAGINAS')
    tv.place(x=480, y=280)

    # conexão
    def conexao():
        con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='root', password='Kamenriderv3')
        cursor = con.cursor()
        query = f'SELECT * FROM bookbox'
        cursor.execute(query)
        data = cursor.fetchall()
        cursor.close()
        con.close()

        for x in data:
            tv.insert("", "end", values=(x[0], x[1], x[2], x[3], x[4], x[5], x[6], x[7]))

    conexao()

    def limpar():
        titulo_entrada.delete(0, END)
        author_entrada.delete(0, END)
        isbn_entrada.delete(0, END)
        publishing_entrada.delete(0, END)
        year_entrada.delete(0, END)
        genre_entrada.delete(0, END)
        pages_entrada.delete(0, END)
        view_entrada.delete(0, END)
        search_entrada.delete(0, END)
        combo.delete(0, END)

    # Funções
    def adicionar():
        global file_encoded

        tit = str(titulo_entrada.get().strip())
        atr = str(author_entrada.get().strip())
        i = str(isbn_entrada.get().strip())
        pub = str(publishing_entrada.get().strip())
        yr = year_entrada.get().strip()
        gr = str(genre_entrada.get().strip())
        pg = pages_entrada.get().strip()

        if (
                titulo_entrada.get() == "" or author_entrada.get() == "" or isbn_entrada.get() == "" or publishing_entrada.get() == ""
                or year_entrada.get() == "" or genre_entrada.get() == "" or pages_entrada.get() == ""):
            messagebox.showerror('Campo Vazio', 'Preencha todos os campos')
            return

        try:
            con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='root',
                                          password='Kamenriderv3')
            cursor = con.cursor()
            args = (f"{tit}", f"{atr}", i, f"{pub}", yr, f"{gr}", pg, file_encoded)
            query = (
                'INSERT INTO bookbox (titulo, autor, ISBN, editora, ano_publicacao, genero, paginas, capa) VALUES (%s, %s, '
                '%s, %s, %s, %s, %s, %s)')

            cursor.execute(query, args)
            con.commit()
            cursor.close()
            con.close()
            limpar()
            atualizar()
            messagebox.showinfo('Novo Registro', 'Adicionado com sucesso')

        except Error as erro:
            messagebox.showerror('Erro', f'{erro}')

    def capa():
        global file_encoded

        file = askopenfilename(filetypes=(('All Files', '*.*'), ('PNG', '*.png'), ('JPG', '*.jpg')))
        if file:
            file_get = open(file, 'rb').read()
            file_encoded = base64.b64encode(file_get)
        else:
            messagebox.showerror('Selecione uma imagem', 'Nenhuma imagem selecionada')
            return

    # Duplo clique
    def duploclique(event):
        limpar()
        tv.selection()

        for x in tv.selection():
            col1, col2, col3, col4, col5, col6, col7, col8 = tv.item(x, 'values')
            view_entrada.insert(END, col1)
            titulo_entrada.insert(END, col2)
            author_entrada.insert(END, col3)
            isbn_entrada.insert(END, col4)
            publishing_entrada.insert(END, col5)
            year_entrada.insert(END, col6)
            genre_entrada.insert(END, col7)
            pages_entrada.insert(END, col8)

    tv.bind('<Double-1>', duploclique)

    def atualizar():
        tv.delete(*tv.get_children())  # get_children faz o refresh da tabela
        conexao()

    def editar():
        id_l = view_entrada.get().strip()
        tit = str(titulo_entrada.get().strip())
        atr = str(author_entrada.get().strip())
        i = str(isbn_entrada.get().strip())
        pub = str(publishing_entrada.get().strip())
        yr = year_entrada.get().strip()
        gr = str(genre_entrada.get().strip())
        pg = pages_entrada.get().strip()

        if (
                view_entrada.get() == "" or titulo_entrada.get() == "" or author_entrada.get() == "" or isbn_entrada.get() == ""
                or publishing_entrada.get() == "" or year_entrada.get() == "" or genre_entrada.get() == "" or pages_entrada.get() == ""):
            messagebox.showerror('Campo Vazio', 'Preencha todos os campos')
            return

        try:
            con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='usuario',
                                          password='usuario2023')
            cursor = con.cursor()
            cursor.execute(f"UPDATE bookbox SET titulo = '{tit}', autor = '{atr}', ISBN = '{i}', editora = '{pub}', "
                           f"ano_publicacao = {yr}, genero = '{gr}', paginas = {pg} WHERE ID_Livro = {id_l}")
            con.commit()
            cursor.close()
            con.close()
            limpar()
            atualizar()
            messagebox.showinfo('Editar', 'Editado com sucesso')

        except Error as erro:
            messagebox.showerror('Erro', f'{erro}')

    def deletar():
        cod = view_entrada.get()

        if view_entrada.get() == "":
            messagebox.showerror('Campo vazio', 'Preencha todos os campos')
            return

        try:
            con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='usuario',
                                          password='usuario2023')

            cursor = con.cursor()
            cursor.execute(f"DELETE FROM bookbox WHERE ID_Livro = '{cod}'")
            con.commit()
            cursor.close()
            con.close()
            limpar()
            atualizar()
            messagebox.showinfo('Excluir', 'Excluído com sucesso')

        except Error as erro:
            messagebox.showerror('Erro', f'{erro}')

    def consultar():
        global img
        escolha = view_entrada.get()

        if view_entrada.get() == "":
            messagebox.showerror('Campo vazio', 'Preencha o ID')
            return

        try:
            con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='root',
                                          password='Kamenriderv3')
            cursor = con.cursor()
            query = f"SELECT * FROM bookbox WHERE ID_Livro='{escolha}'"
            cursor.execute(query)
            dados = cursor.fetchall()
            cursor.close()
            con.close()

            new_root = Toplevel()
            new_root.title('Consulta')
            new_root.geometry('900x500')
            new_root.config(bg='#072a4d')
            new_root.resizable(width=False, height=True)
            btn_voltar = Button(new_root, text='Fechar', relief='raised', width=8, height=1, bg='orange', fg='white',
                                font='Arial 10 bold', command=new_root.destroy)
            btn_voltar.place(x=520, y=360)

            for x in dados:
                # Decodificar imagem
                binary_data = base64.b64decode((x[8]))
                # Converta os bytes em uma imagem PIL
                image = Image.open(io.BytesIO(binary_data))
                # Redimensionando a imagem
                resized_image = image.resize((300, 430))
                img = ImageTk.PhotoImage(resized_image)
                cover = Label(master=new_root, image=img)
                cover.place(x=10, y=10)

                tit = Label(new_root, width=8, height=1, text='Título:', font='Arial 10 bold', relief='flat',
                            bg='#072a4d',
                            fg='yellow',
                            anchor=W)
                tit.place(x=330, y=20)
                titulo = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                               anchor=W)
                titulo.place(x=410, y=20)
                titulo['text'] = (x[1])

                aut = Label(new_root, width=8, height=1, text='Autor:', font='Arial 10 bold', relief='flat',
                            bg='#072a4d',
                            fg='yellow',
                            anchor=W)
                aut.place(x=330, y=60)
                autor = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                              anchor=W)
                autor.place(x=410, y=60)
                autor['text'] = (x[2])

                isbn = Label(new_root, width=8, height=1, text='ISBN:', font='Arial 10 bold', relief='flat',
                             bg='#072a4d',
                             fg='yellow',
                             anchor=W)
                isbn.place(x=330, y=100)
                isbn_n = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                               anchor=W)
                isbn_n.place(x=410, y=100)
                isbn_n['text'] = (x[3])

                ed = Label(new_root, width=8, height=1, text='Editora:', font='Arial 10 bold', relief='flat',
                           bg='#072a4d',
                           fg='yellow',
                           anchor=W)
                ed.place(x=330, y=140)
                editora = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                                anchor=W)
                editora.place(x=410, y=140)
                editora['text'] = (x[4])

                an = Label(new_root, width=8, height=1, text='Ano:', font='Arial 10 bold', relief='flat', bg='#072a4d',
                           fg='yellow',
                           anchor=W)
                an.place(x=330, y=180)
                ano_p = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                              anchor=W)
                ano_p.place(x=410, y=180)
                ano_p['text'] = (x[5])

                gen = Label(new_root, width=8, height=1, text='Gênero:', font='Arial 10 bold', relief='flat',
                            bg='#072a4d',
                            fg='yellow',
                            anchor=W)
                gen.place(x=330, y=220)
                genero = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                               anchor=W)
                genero.place(x=410, y=220)
                genero['text'] = (x[6])

                pgs = Label(new_root, width=8, height=1, text='Páginas:', font='Arial 10 bold', relief='flat',
                            bg='#072a4d',
                            fg='yellow',
                            anchor=W)
                pgs.place(x=330, y=260)
                paginas = Label(new_root, width=40, height=1, relief='solid', font='Arial 10', fg='black', bg='white',
                                anchor=W)
                paginas.place(x=410, y=260)
                paginas['text'] = (x[7])

            limpar()

        except Error as erro:
            messagebox.showerror('Erro', f'{erro}')

    def pesquisar():
        if combo.get() == "":
            messagebox.showerror('Erro', 'Escolha um parâmetro para pesquisa')
            return

        con = mysql.connector.connect(host='localhost', database='db_Biblioteca', user='root', password='Kamenriderv3')
        if combo.get() == 'Título':
            tv.delete(*tv.get_children())
            pesq_titulo = search_entrada.get().strip().title()
            dados = f'SELECT * FROM bookbox WHERE titulo REGEXP "^{pesq_titulo}"'
            cursor = con.cursor()
            cursor.execute(dados)
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            for i in resultado:
                tv.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        if combo.get() == 'Autor':
            tv.delete(*tv.get_children())
            pesq_autor = search_entrada.get().strip().title()
            dados = f'SELECT * FROM bookbox WHERE autor REGEXP "^{pesq_autor}"'
            cursor = con.cursor()
            cursor.execute(dados)
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            for i in resultado:
                tv.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        if combo.get() == 'Editora':
            tv.delete(*tv.get_children())
            pesq_editora = search_entrada.get().strip().title()
            dados = f'SELECT * FROM bookbox WHERE editora REGEXP "^{pesq_editora}"'
            cursor = con.cursor()
            cursor.execute(dados)
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            for i in resultado:
                tv.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        if combo.get() == 'Gênero':
            tv.delete(*tv.get_children())
            pesq_genero = search_entrada.get().strip().title()
            dados = f'SELECT * FROM bookbox WHERE genero REGEXP "^{pesq_genero}"'
            cursor = con.cursor()
            cursor.execute(dados)
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            for i in resultado:
                tv.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))

        if combo.get() == 'ISBN':
            tv.delete(*tv.get_children())
            pesq_isbn = search_entrada.get().strip().title()
            dados = f'SELECT * FROM bookbox WHERE ISBN REGEXP "^{pesq_isbn}"'
            cursor = con.cursor()
            cursor.execute(dados)
            resultado = cursor.fetchall()
            cursor.close()
            con.close()

            for i in resultado:
                tv.insert("", "end", values=(i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7]))
        limpar()

    def mostrar_todos():
        tv.delete(*tv.get_children())
        limpar()
        conexao()

    # Botões
    btn_capa = Button(frame1, command=capa, text='Escolher capa', width=30, height=1, relief='raised',
                      font='Arial 10 bold',
                      fg='white',
                      bg='#34b4eb')
    btn_capa.place(x=70, y=660)

    btn_create = Button(frame1, command=adicionar, width=8, height=1, text='Adicionar', font='Arial 10 bold',
                        relief='raised',
                        fg='white', bg='blue')
    btn_create.place(x=50, y=730)

    btn_update = Button(frame1, command=editar, width=8, height=1, text='Editar', font='Arial 10 bold',
                        relief='raised',
                        fg='white', bg='green')
    btn_update.place(x=150, y=730)

    btn_delete = Button(frame1, command=deletar, width=8, height=1, text='Deletar', font='Arial 10 bold',
                        relief='raised',
                        fg='white', bg='red')
    btn_delete.place(x=250, y=730)

    btn_read = Button(frame2, command=consultar, width=9, height=1, text='Visualizar', font='Arial 10 bold',
                      relief='raised',
                      fg='white',
                      bg='#26ab31')
    btn_read.place(x=320, y=120)

    btn_search = Button(frame2, command=pesquisar, relief='raised', text='Pesquisar', font='Arial 10 bold', bg='orange',
                        fg='white', width=8, height=1)
    btn_search.place(x=620, y=35)

    btn_todos = Button(frame2, command=mostrar_todos, relief='raised', text='Mostrar Todos', font='Arial 10 bold',
                       bg='orange', fg='white', width=12,
                       height=1)
    btn_todos.place(x=720, y=35)

    root.mainloop()
