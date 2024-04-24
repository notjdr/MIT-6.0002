import sqlite3
connection= sqlite3.connect('sqlite.db')
cursor = connection.cursor()
cursor.execute('''CREATE TABLE if not Exists UAE
               (Name text, Country text, Height real, Weight real)''')

athelete_name = 'JOÃO ALMEIDA'
athelete_country = 'PORTUGAL'
athlete_height = 1.78
athlete_weight = 63


INSERT_QUERY = f"INSERT INTO UAE VALUES ('{athelete_name}','{athelete_country}','{athlete_height}','{athlete_weight}')"
cursor.execute(INSERT_QUERY)

for row in cursor.execute('SELECT * FROM UAE'):
    print(row)

# Save (commit) the changes
connection.commit()
# close connection
connection.close() 