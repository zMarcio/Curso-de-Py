# pip install --upgrade 'sqlalchemy<2.0'
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

data = pd.read_csv('https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv')
print(data)

data.to_sql('Cliente', engine, index=False)

print(data)

query_1 = 'UPDATE Cliente SET Rendimento_anual=300000.0 WHERE ID_Cliente=6840104'
query_2 = 'DELETE Cliente WHERE ID_Cliente=5008809'
query_3 = 'INSERT INTO cliente (ID_Cliente, Idade, Grau_escolaridade, Estado_civil, ' \
        'Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, ' \
        'Rendimento_anual, Tem_carro, Moradia) ' \
        'VALUES (6850985, 33, "Doutorado", "Solteiro", 1, "Empregado", "TI", ' \
        '2, 290000, 0, "Casa/apartamento próprio")'

with engine.connect() as conn:
  conn.execute(query_1)

pd.read_sql('Cliente', engine)

with engine.connect() as conn:
  conn.execute(query_2)

pd.read_sql('Cliente', engine)

with engine.connect() as conn:
  conn.execute(query_3)

pd.read_sql('Cliente', engine)

query = 'SELECT * FROM Cliente WHERE ID_Cliente=6850985'

pd.read_sql(query,engine)