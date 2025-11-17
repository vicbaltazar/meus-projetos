import sqlite3

#Criando banco de dados
conexao = sqlite3.connect('amor_doce.db')
cursor = conexao.cursor()

#Tabela de personagens
cursor.execute("""
CREATE TABLE IF NOT EXISTS personagens (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    relacoes TEXT,
    aparicao_inicial TEXT,
    caracteristicas TEXT
)
""")

#Inserir personagens
personagens = [
    ("Ambre", "Estudante da Escola Sweet Amoris, Vaidosa", "Irmã do Nathaniel", "Episódio inicial", "Vaidosa e Popular"),
    ("Castiel", "Um dos paqueras principais", "Melhor amigo do Lysandre", "Episódio inicial", "Popular e Esportivo"),
    ("Lysandre", "Calmo, educado e sempre com um caderninho", "Irmão do Leigh", "Episódio 4", "Misterioso e Reservado"),
    ("Violette", "Tímida, amante da arte, melancólica", "Amiga da Kim, Docete e Alexy", "Episódio 4", "Talentosa em desenhos"),
    ("Melody", "Gosta do Nathaniel, amiga dele", "Amiga do Nathaniel", "Episódio 7", "Talentosa")
]

cursor.executemany("""
INSERT INTO personagens (nome, descricao, relacoes, aparicao_inicial, caracteristicas)
VALUES (?, ?, ?, ?, ?)
""", personagens)

conexao.commit()

#Mostrar personagens
cursor.execute('SELECT * FROM personagens')
for linha in cursor.fetchall():
    print(linha)

#fechar
conexao.close()