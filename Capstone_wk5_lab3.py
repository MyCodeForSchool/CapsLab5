"""
A menu - you need to add the database and fill in the functions.
"""
import sqlite3

conn = sqlite3.connect('chainsaw_rcds.sqlite')

conn.execute('CREATE TABLE IF NOT EXISTS records (name TEXT UNIQUE, country TEXT, nbr_caught INT)')
conn.commit()
# TODO create database table OR set up Peewee model to create table

def main():
    menu_text = """
    1. Display all records
    2. Search by name
    3. Add new record
    4. Edit existing record
    5. Delete record 
    6. Quit
    """

    while True:
        print(menu_text)
        choice = input('Enter your choice: ')
        if choice == '1':
            display_all_records()
        elif choice == '2':
            search_by_name()
        elif choice == '3':
            add_new_record()
        elif choice == '4':
            edit_existing_record()
        elif choice == '5':
            delete_record()
        elif choice == '6':
            break
        else:
            print('Not a valid selection, please try again')


def display_all_records():
    results = conn.execute('SELECT * FROM records')

    for row in results:
        print(row)
    #print('todo display all records')


def search_by_name():
    search_name = input('Enter a name to search for: ')
    results = conn.execute('SELECT * FROM records WHERE name = ?', (search_name,))

    for row in results:
        print(row)
    #print('todo ask user for a name, and print the matching record if found. What should the program do if the name is not found?')


def add_new_record():
    new_name = input('Enter new name: ')
    new_country = input('Enter new country: ')
    new_nbr_caught = int(input('Enter the number of chainsaws caught: '))

    try:
        conn.execute(f'INSERT INTO records (name, country, nbr_caught) VALUES (?, ?, ?)', (new_name, new_country, new_nbr_caught))
        conn.commit()
    except:
        print('Record already exists.  Please select a new action.')


def edit_existing_record():
    update_name = input('Enter a name to edit: ')
    new_country = input('Enter new country: ')
    new_nbr_caught = int(input('Enter number of chainsaws caught: '))
    conn.execute(f'UPDATE records SET country = ? SET nbr_caught = ? WHERE name = ?', (new_country, new_nbr_caught, update_name))
    print('todo edit existing record. What if user wants to edit record that does not exist?')


def delete_record():
    print('todo delete existing record. What if user wants to delete record that does not exist?')


if __name__ == '__main__':
    main()