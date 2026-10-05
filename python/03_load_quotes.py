import os
import time
from pathlib import Path

import psycopg
from dotenv import load_dotenv


load_dotenv()

CSV_FILE = Path(__file__).parent / "quotes_500k.csv"

inicio = time.perf_counter()

conn = psycopg.connect(
    host=os.getenv("POSTGRES_HOST"),
    port=os.getenv("POSTGRES_PORT"),
    dbname=os.getenv("POSTGRES_DB"),
    user=os.getenv("POSTGRES_USER"),
    password=os.getenv("POSTGRES_PASSWORD")
)

with conn.cursor() as cur:
    with CSV_FILE.open("r", encoding="utf-8") as arquivo:
        with cur.copy("""
            COPY cotacoes_historicas
                (ativo_id, data_hora, preco_abertura, preco_fechamento, volume)
            FROM STDIN
            WITH (FORMAT CSV)
        """) as copy:
            while data := arquivo.read(8192):
                copy.write(data)

conn.commit()
conn.close()

fim = time.perf_counter()

print("Dados carregados com sucesso!")
print("Registros: 500.000")
print(f"Tempo de carga: {fim - inicio:.2f} segundos")