import sqlite3

db = 'products.sqlite'

with sqlite3.connect(db) as conn:
    #conn.execute('CREATE TABLE IF NOT EXISTS products (name TEXT UNIQUE, quantity INT)')
    #use above to create and use row id as primary key
    conn.execute('CREATE TABLE IF NOT EXISTS products (product_id INTEGER PRIMARY KEY, name TEXT UNIQUE, quantity INT)')
conn.close()

name = 'hat'
quantity = 2

try:
    with sqlite3.connect(db) as conn:
        conn.execute('INSERT INTO products (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.close()
except Exception as e:
    print('Error inserting ', e)

conn = sqlite3.connect(db)
# results = conn.execute('SELECT rowid, * FROM products')
    #autoadds a row id that autoincrements or use primary key specifications
    #in your code like above
results = conn.execute('SELECT * FROM products')
for row in results:
    print(row)

print('End of Program')
# results = conn.execute('SELECT * FROM products')
#
# for row in results:
#     print(row) #each row is a tuple