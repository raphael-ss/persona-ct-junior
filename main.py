import sqlite3
import csv

# Conecta à base de dados (cria uma se não existir)
conn = sqlite3.connect("persona.sqlite")
cursor = conn.cursor()

# Cria uma tabela 
cria_query_tabela = """
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
"""

cursor.execute(cria_query_tabela)

# Abra o arquivo CSV e leia
with open("persona_tec.csv", "r") as persona_tec:
    csv_reader = csv.reader(persona_tec)
    next(csv_reader)  # pula linha de especificação (header)

    for row in csv_reader:
        print(row)
        cliente = row[0]
        print(cliente)
        instancias = cliente.split(';')
        print(instancias)
        cursor.execute(f"""INSERT INTO persona (id, name_client, gender, close_year, phone, has_company, name_company, company_field, cpf_cnpj, sector, services, source, price, origin_place, social_capital, n_of_services, total_price) VALUES 
                       ({int(instancias[0])}, '{instancias[1]}', '{instancias[2]}', {int(instancias[3])}, '{instancias[4]}', {int(instancias[5])}, '{instancias[6]}', '{instancias[7]}', '{instancias[8]}', '{instancias[9]}', '{instancias[10]}', '{instancias[11]}',
                       '{instancias[12]}', '{instancias[13]}', {int(instancias[14])}, {int(instancias[15])}, {int(instancias[16])});""")

# Commit das mudanças e encerre a conexão
conn.commit()
conn.close()
