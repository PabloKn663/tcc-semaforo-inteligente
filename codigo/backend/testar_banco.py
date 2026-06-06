import sqlite3

conexao = sqlite3.connect("banco_de_dados/semaforo_inteligente.db")
cursor = conexao.cursor()

cursor.execute("""
INSERT INTO cruzamento (nome, localizacao)
VALUES ('Cruzamento 1', 'Via principal com via secundária')
""")

cursor.execute("""
INSERT INTO fluxo_trafego (id_cruzamento, quantidade_veiculos)
VALUES (1, 18)
""")

cursor.execute("""
INSERT INTO decisao_ia (
    id_cruzamento,
    quantidade_veiculos,
    tempo_padrao,
    tempo_calculado,
    emergencia_detectada
)
VALUES (1, 18, 20, 34, 0)
""")

conexao.commit()

cursor.execute("SELECT * FROM decisao_ia")
dados = cursor.fetchall()

print("Registros salvos no banco:")
for linha in dados:
    print(linha)

conexao.close()