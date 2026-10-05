import csv
import random
import time
from datetime import datetime, timedelta
from pathlib import Path


OUTPUT_FILE = Path(__file__).parent / "quotes_500k.csv"

ATIVOS = {
    1: 38.50,   # PETR4
    2: 62.30,   # VALE3
    3: 35.80,   # ITUB4
    4: 160.50,  # HGLG11
    5: 120.00,  # IVVB11
}

TOTAL_REGISTROS = 500_000

data_inicial = datetime(2025, 1, 1, 10, 0, 0)

inicio = time.perf_counter()

with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)

    for i in range(TOTAL_REGISTROS):
        ativo_id = random.choice(list(ATIVOS.keys()))
        preco_base = ATIVOS[ativo_id]

        data_hora = data_inicial + timedelta(minutes=i * 5)

        variacao_abertura = random.uniform(-0.03, 0.03)
        preco_abertura = preco_base * (1 + variacao_abertura)

        variacao_fechamento = random.uniform(-0.02, 0.02)
        preco_fechamento = preco_abertura * (1 + variacao_fechamento)

        volume = random.randint(1000, 500000)

        writer.writerow([
            ativo_id,
            data_hora.strftime("%Y-%m-%d %H:%M:%S"),
            round(preco_abertura, 4),
            round(preco_fechamento, 4),
            volume
        ])

fim = time.perf_counter()

print(f"{TOTAL_REGISTROS:,} registros gerados.")
print(f"Arquivo: {OUTPUT_FILE}")
print(f"Tempo de geração: {fim - inicio:.2f} segundos")