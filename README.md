# PostgreSQL Lab

Laboratório prático para estudos de PostgreSQL, SQL analítico, Python e performance de consultas.

## Objetivo

Projeto desenvolvido para praticar conceitos de bancos de dados relacionais e análise de dados utilizando PostgreSQL e Python.

O laboratório simula um pequeno ambiente relacionado ao mercado de investimentos, com foco em:

- Modelagem de dados
- SQL e consultas analíticas
- Window Functions
- Índices e performance
- Transações
- Integração entre Python e PostgreSQL
- Carga e análise de grandes volumes de dados

## Tecnologias

- PostgreSQL 17
- Python
- Psycopg
- Docker
- Docker Compose
- SQL

## Estrutura

```text
PostgreSQL-Lab/
├── python/
│   ├── 01_test_connection.py
│   ├── 02_generate_quotes.py
│   └── 03_load_quotes.py
│
├── sql/
│   └── 01_schema.sql
│
├── .env
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

> O arquivo `.env` é utilizado apenas localmente e não é versionado.

## O que foi praticado

### SQL

- SELECT, WHERE e ORDER BY
- GROUP BY e HAVING
- JOINs
- CTEs
- Funções de agregação
- Chaves primárias e estrangeiras
- Restrições de integridade

### Análise de dados

- Window Functions
- `LAG()`
- `ROW_NUMBER()`
- Análise de variação de preços
- Ranking de movimentações

### Performance

Foi utilizado `EXPLAIN ANALYZE` para analisar consultas antes e depois da criação de índices.

Em um dos testes realizados:

```text
Antes do índice: 26.420 ms
Depois do índice: 2.920 ms
```

### Python

Python foi utilizado para:

- Conectar ao PostgreSQL
- Gerar 500.000 registros
- Carregar dados em grande volume
- Automatizar tarefas relacionadas ao banco

## Como executar

Inicie o PostgreSQL com Docker:

```bash
docker compose up -d
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Teste a conexão:

```bash
python python/01_test_connection.py
```

Para gerar os dados:

```bash
python python/02_generate_quotes.py
```

Para carregar os dados no PostgreSQL:

```bash
python python/03_load_quotes.py
```

## Próximos passos

- Novas consultas analíticas
- Mais experimentos de performance
- Diferentes tipos de índices
- Particionamento
- Novos scripts de análise
- Integração com APIs