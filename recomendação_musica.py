import sqlite3

#criando banco de dados
conexao = sqlite3.connect("selvagens.db")
cursor = conexao.cursor()

#tabela de musica
cursor.execute("""
CREATE TABLE IF NOT  EXISTS musica (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    artista TEXT NOT NULL,
    genero TEXT NOT NULL
)
""")
conexao.commit()

#musicas Selvagens à Procura de Lei
musicas_selvagens = [
    ("Massarrara", "Selvagens à Procura de Lei", "Rock Nacional"), #1
    ("Despedida", "Selvagens à Procura de Lei", "Rock Nacional"), #2
    ("Mar Fechado", "Selvagens à Procura de Lei", "Rock Nacional"), #3
    ("Casona", "Selvagens à Procura de Lei", "Rock Nacional"), #4
    ("Juventude Solitude", "Selvagens à Procura de Lei", "Rock Nacional"), #5
    ("Tarde Livre", "Selvagens à Procura de Lei", "Rock Nacional"), #6
    ("Gostar Só Dela", "Selvagens à Procura de Lei", "Rock Nacional"), #7
    ("Sede ao Pote", "Selvagens à Procura de Lei", "Rock Nacional"), #8
    ("Mucambo Cafundó", "Selvagens à Procura de Lei", "Rock Nacional"), #9
    ("Semana Passada", "Selvagens à Procura de Lei", "Rock Nacional"), #10
]

#inserindo musicas
cursor.executemany("""
INSERT INTO musica (titulo, artista, genero)
VALUES (?, ?, ?)
""", musicas_selvagens)
conexao.commit()

#consultando
cursor.execute("SELECT * FROM musica")
for musica in cursor.fetchall():
    print(musica)

#fechando
conexao.close()