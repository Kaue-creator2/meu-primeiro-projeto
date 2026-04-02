import sqlite3

conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS tarefas (
               id INTEGER PRIMARY KEY,
               descricao TEXT,
               concluida BOOLEAN
        )
""")

conexao.commit()
print("Tabela criada")
conexao.close()



conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("INSERT INTO tarefas (descricao, concluida) VALUES (?, ?)",
               ("Estudar Python", False))

conexao.commit()
print("Tarefa adicionada")
conexao.close()


conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM tarefas")
tarefas = cursor.fetchall()

for tarefa in tarefas:
    print(tarefa)

conexao.close()


conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("DELETE FROM tarefas WHERE id =?", (1,))

conexao.commit()
print("Tarefa deletada")
conexao.close()


conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM tarefas")
tarefas = cursor.fetchall()

print("tarefas restantes:")
for tarefa in tarefas:
    print(tarefa)
    
conexao.close()

conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("UPDATE tarefas SET concluida = 1 WHERE id = 2")

conexao.commit()
print("tarefa atualizada")
conexao.close()


conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("SELECT * FROM tarefas WHERE concluida = 1")
tarefas = cursor.fetchall()

print("Tarefas concluidas:")
for tarefa in tarefas:
    print(tarefa)

    conexao.close