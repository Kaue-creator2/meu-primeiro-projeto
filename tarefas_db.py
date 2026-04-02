import sqlite3

def conectar():
    return sqlite3.connect("tarefas.db")

def criar_tabela():
    con = conectar()
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY,
            descricao TEXT,
            concluida INTEGER
        )
    """)
    con.commit()
    con.close()

def adicionar(descricao):
    con = conectar()
    cur = con.cursor()
    cur.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?,0)", (descricao,))
    con.commit()
    con.close()
    print("tarefas adicionadas")

def ver_tarefas():
    con = conectar()
    cur = con.cursor()
    cur.execute("SELECT * FROM tarefas")
    tarefas = cur.fetchall()
    con.close()
    if len(tarefas) == 0:
            print("Nenhuma tarefa")
    else:
            for t in tarefas:
                        print(f"{t[0]}. {t[1]}")

                        criar_tabela()

while True:
    print("\n1. Adicionar")
    print("2. Ver tarefas")
    print("3. Sair")
    opcao = input("Opcao: ")

    if opcao == "1":
            desc = input("Tarefa: ")
            adicionar(desc)
    elif opcao == "2":
            ver_tarefas()
    elif opcao == "3":
          break