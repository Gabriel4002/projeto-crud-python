from interface import Gui
import Backend as core
from tkinter import END

app = None
selected = None

def view_command():
    rows = core.view()
    app.listClientes.delete(0, END)
    for r in rows:
        app.listClientes.insert(END, r)


def search_command():
    app.listClientes.delete(0, END)  # Limpa a lista

    rows = core.search(app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())

    if rows:
        for r in rows:
            app.listClientes.insert(END, r)
    else:
        app.listClientes.insert(END, "Nenhum resultado encontrado.")


def insert_command():
    nome = app.txtNome.get()
    sobrenome = app.txtSobrenome.get()
    email = app.txtEmail.get()
    cpf = app.txtCPF.get()

    # Verifica se todos os campos estão preenchidos
    if not nome.strip() or not sobrenome.strip() or not email.strip() or not cpf.strip():
        # Exibe a mensagem de erro na Listbox apenas uma vez
        app.listClientes.delete(0, END)  # Limpa a lista antes de adicionar a mensagem
        app.listClientes.insert(END, "Preencha todos os campos")
        return  # Retorna se algum campo estiver vazio

    try:
        # Tenta inserir os dados no banco
        core.insert(nome, sobrenome, email, cpf)
        print("Dados inseridos com sucesso.")
        view_command()  # Atualiza a visualização
    except Exception as e:
        # Se ocorrer algum erro, exibe uma mensagem
        print(f"Erro ao inserir os dados: {e}")
        app.listClientes.delete(0, END)  # Limpa a lista antes de adicionar a mensagem de erro
        app.listClientes.insert(END, f"Erro: {e}")

def update_command():
    if selected:  # Verifica se 'selected' não é None
        core.update(selected[0], app.txtNome.get(), app.txtSobrenome.get(), app.txtEmail.get(), app.txtCPF.get())
        view_command()
    else:
        app.listClientes.insert(END, "Nenhum item selecionado para atualizar.")

def del_command():
    if selected:  # Verifica se 'selected' não é None
        id_selected = selected[0]
        core.delete(id_selected)
        view_command()
    else:
        app.listClientes.insert(END, "Nenhum item selecionado para deletar.")

def getSelectedRow(event):
    global selected
    index = app.listClientes.curselection()

    # Verifique se um item foi realmente selecionado
    if index:
        index = index[0]  # Pega o primeiro item selecionado
        selected = app.listClientes.get(index)

        # Preenche os campos de entrada com os valores do item selecionado
        app.entNome.delete(0, END)
        app.entNome.insert(END, selected[1])

        app.entSobrenome.delete(0, END)
        app.entSobrenome.insert(END, selected[2])

        app.entEmail.delete(0, END)
        app.entEmail.insert(END, selected[3])

        app.entCPF.delete(0, END)
        app.entCPF.insert(END, selected[4])
    else:
        selected = None  # Se não houver seleção, definimos selected como None


if __name__ == "__main__":
    app = Gui()

    app.listClientes.bind('<<ListboxSelect>>', getSelectedRow)

    app.btnViewAll.configure(command=view_command)
    app.btnBuscar.configure(command=search_command)
    app.btnInserir.configure(command=insert_command)
    app.btnUpdate.configure(command=update_command)
    app.btnDel.configure(command=del_command)
    app.btnClose.configure(command=app.window.destroy)

    app.run()
