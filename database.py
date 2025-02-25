import sqlite3

def create_database():
    try:
        conn = sqlite3.connect('dog_breeds.db')
        cur = conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS breeds (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed_group TEXT,
                life_span TEXT,
                temperament TEXT,
                origin TEXT
            )
        ''')
        conn.commit()
        print("Database and table created successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def insert_breed(breed):
    try:
        conn = sqlite3.connect('dog_breeds.db')
        cur = conn.cursor()
        cur.execute('''
            INSERT INTO breeds (name, breed_group, life_span, temperament, origin)
            VALUES (?, ?, ?, ?, ?)
        ''', breed)
        conn.commit()
        print("Breed inserted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def read_breed_by_id(breed_id):
    try:
        conn = sqlite3.connect('dog_breeds.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM breeds WHERE id=?', (breed_id,))
        breed = cur.fetchone()
        return breed
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def update_breed(breed):
    try:
        conn = sqlite3.connect('dog_breeds.db')
        cur = conn.cursor()
        cur.execute('''
            UPDATE breeds
            SET name = ?, breed_group = ?, life_span = ?, temperament = ?, origin = ?
            WHERE id = ?
        ''', breed)
        conn.commit()
        print("Breed updated successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def delete_breed(breed_id):
    try:
        conn = sqlite3.connect('dog_breeds.db')
        cur = conn.cursor()
        cur.execute('DELETE FROM breeds WHERE id=?', (breed_id,))
        conn.commit()
        print("Breed deleted successfully.")
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()

def search_breed_by_name(name):
    try:
        conn = sqlite3.connect('dog_breeds.db')
        cur = conn.cursor()
        cur.execute('SELECT * FROM breeds WHERE name LIKE ?', ('%' + name + '%',))
        breeds = cur.fetchall()
        return breeds
    except sqlite3.Error as e:
        print(f"SQLite error: {e}")
    finally:
        if conn:
            conn.close()