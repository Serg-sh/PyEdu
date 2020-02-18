import sqlalchemy


print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/testdb')

connection = engine.connect()

result = connection.execute("SELECT * FROM superheroes")

for row in result:
    print('Hero_name', row['hero_name'])

result.close()


