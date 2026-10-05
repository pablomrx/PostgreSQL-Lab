CREATE TABLE investidores (
    id BIGSERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    perfil_risco VARCHAR(20) NOT NULL,
    saldo NUMERIC(15, 2) NOT NULL DEFAULT 0,

    CONSTRAINT chk_investidor_perfil_risco
        CHECK (perfil_risco IN ('CONSERVADOR', 'MODERADO', 'ARROJADO')),

    CONSTRAINT chk_investidor_saldo
        CHECK (saldo >= 0)
);


CREATE TABLE ativos (
    id BIGSERIAL PRIMARY KEY,
    ticker VARCHAR(10) NOT NULL UNIQUE,
    tipo VARCHAR(20) NOT NULL,
    setor VARCHAR(50),

    CONSTRAINT chk_ativo_tipo
        CHECK (tipo IN ('ACAO', 'FII', 'ETF', 'CRIPTO'))
);


CREATE TABLE ordens_executadas (
    id BIGSERIAL PRIMARY KEY,
    investidor_id BIGINT NOT NULL,
    ativo_id BIGINT NOT NULL,
    tipo VARCHAR(10) NOT NULL,
    quantidade INTEGER NOT NULL,
    preco NUMERIC(15, 4) NOT NULL,
    data_hora TIMESTAMP NOT NULL,

    CONSTRAINT fk_ordem_investidor
        FOREIGN KEY (investidor_id)
        REFERENCES investidores(id),

    CONSTRAINT fk_ordem_ativo
        FOREIGN KEY (ativo_id)
        REFERENCES ativos(id),

    CONSTRAINT chk_ordem_tipo
        CHECK (tipo IN ('COMPRA', 'VENDA')),

    CONSTRAINT chk_ordem_quantidade
        CHECK (quantidade > 0),

    CONSTRAINT chk_ordem_preco
        CHECK (preco > 0)
);


CREATE TABLE cotacoes_historicas (
    id BIGSERIAL PRIMARY KEY,
    ativo_id BIGINT NOT NULL,
    data_hora TIMESTAMP NOT NULL,
    preco_abertura NUMERIC(15, 4) NOT NULL,
    preco_fechamento NUMERIC(15, 4) NOT NULL,
    volume BIGINT NOT NULL,

    CONSTRAINT fk_cotacao_ativo
        FOREIGN KEY (ativo_id)
        REFERENCES ativos(id),

    CONSTRAINT chk_cotacao_abertura
        CHECK (preco_abertura > 0),

    CONSTRAINT chk_cotacao_fechamento
        CHECK (preco_fechamento > 0),

    CONSTRAINT chk_cotacao_volume
        CHECK (volume >= 0)
);