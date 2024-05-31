import pandas as pd
import sqlalchemy

from sqlalchemy import create_engine, MetaData, Table, inspect

engine = create_engine('sqlite:///:memory:')

url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'
dados = pd.read_csv(url)
dados.head()

dados.to_sql('Clientes',engine,index=False)

inspector = inspect(engine)
print(inspector.get_table_names())

query = 'SELECT * FROM clientes WHERE Categoria_de_renda="Empregado"'

empregados = pd.read_sql(query, engine)

empregados.to_sql('Empregados', con=engine, index=False)

pd.read_sql_table('Empregados', engine)

pd.read_sql_table('Empregados',engine,columns=['ID_Cliente','Grau_escolaridade','Rendimento_anual'])

query = 'SELECT * FROM clientes'

pd.read_sql(query,engine)

query = 'DELETE FROM clientes WHERE ID_Cliente=5008804'

with engine.connect() as conn:
  conn.execute(query)


pd.read_sql_table('Clientes', engine)

query = 'UPDATE clientes SET Grau_escolaridade="Ensino Superior" WHERE ID_Cliente=5008808'

with engine.connect() as conn:
  conn.execute(query)

pd.read_sql_table('Clientes', engine)