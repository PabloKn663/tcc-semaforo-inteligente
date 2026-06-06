import sqlite3
from pathlib import Path

caminho_sql = Path("banco_de_dados/modelo_banco.sql")
caminho_banco = Path("banco_de_dados/semaforo_inteligente.db")

def criar_banco():
    if not caminho_sql.exists():
        print("Erro: arquivo modelo_banco.sql não encontrado.")
        return

    if caminho_banco.exists():
        caminho_banco.unlink()
        print("Banco antigo apagado.")

    conexao = sqlite3.connect(caminho_banco)

    with open(caminho_sql, "r", encoding="utf-8") as arquivo:
        comandos_sql = arquivo.read()

    conexao.executescript(comandos_sql)
    conexao.commit()
    conexao.close()

    print("Banco de dados criado com sucesso!")
    print(f"Arquivo gerado em: {caminho_banco}")

if __name__ == "__main__":
    criar_banco()