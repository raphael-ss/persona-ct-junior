CREATE TABLE persona (
    id INTEGER PRIMARY KEY,
    name_client TEXT NOT NULL,
    gender TEXT,
    close_year TEXT NOT NULL,
    phone TEXT,
    has_company INTEGER NOT NULL,
    name_company TEXT,
    company_field TEXT,
    cpf_cnpj TEXT NOT NULL,
    sector TEXT NOT NULL,
    services TEXT NOT NULL,
    source TEXT DEFAULT Ativa,
    price TEXT NOT NULL,
    origin_place TEXT DEFAULT ES,
    social_capital INTEGER DEFAULT 0,
    n_of_services INTEGER DEFAULT 1,
    total_price INTEGER NOT NULL
);