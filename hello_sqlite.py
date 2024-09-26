import sqlite3

conn = sqlite3.connect('first_db.sqlite')

conn.execute('CREATE TABLE IF NOT EXISTS products(id int, name text)')

# conn.execute('INSERT INTO products VALUES(1000, "hat")')
# conn.execute('INSERT INTO products VALUES(1001, "jacket")')

conn.commit()

results = conn.execute('SELECT * FROM products')

for row in results:
    print(row) #each row is a tuple

# new_id = int(input('Enter new id: '))
# new_name = input('Enter new product: ')
#
# conn.execute(f'INSERT INTO products (id, name) VALUES (?, ?)', (new_id, new_name))
# conn.commit()

# updated_product = 'wool hat'
# update_id = 1000
# conn.execute('UPDATE products SET name = ? WHERE id = ?', (updated_product, update_id))
# conn.commit()

# delete_product = 'jacket'
# conn.execute(f'DELETE FROM products WHERE name=?',(delete_product,))
# conn.commit()

conn.close()
