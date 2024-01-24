import sqlite3

# Connect to SQLite database (or create it if not exists)
conn = sqlite3.connect('PetPuja.db')
cursor = conn.cursor()

# Create customers table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(255),
        password VARCHAR(255)
    )
''')

# Create canteen table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS canteen (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        email VARCHAR(255),
        phone VARCHAR(255),
        password VARCHAR(255)
    )
''')

# Create Prepared_dishes table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Prepared_dishes (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        price INTEGER,
        stock_present INTEGER,
        canteen_id INTEGER,
        FOREIGN KEY (canteen_id) REFERENCES canteen(id)
    )
''')

# Create dishes_to_be_prepared table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS dishes_to_be_prepared (
        id INTEGER PRIMARY KEY,
        name VARCHAR(255),
        prep_time_inmins INTEGER,
        inc_factor FLOAT,
        price INTEGER,
        stock_present INTEGER,
        canteen_id INTEGER,
        FOREIGN KEY (canteen_id) REFERENCES canteen(id)
    )
''')

# Create payment table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS payment (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        amount INTEGER,
        time TIMESTAMP,
        FOREIGN KEY (customer_id) REFERENCES customers(id)
    )
''')

# Create orders table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        dish_id INTEGER,
        quantity INTEGER,
        payment_id INTEGER,
        status VARCHAR(255),
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (dish_id) REFERENCES dishes_to_be_prepared(id)
    )
''')

# Add an additional FOREIGN KEY constraint for Prepared_dishes
cursor.execute('''
    CREATE TABLE IF NOT EXISTS orders_Prepared_dishes (
        id INTEGER PRIMARY KEY,
        customer_id INTEGER,
        dish_id INTEGER,
        quantity INTEGER,
        payment_id INTEGER,
        status VARCHAR(255),
        FOREIGN KEY (customer_id) REFERENCES customers(id),
        FOREIGN KEY (dish_id) REFERENCES Prepared_dishes(id)
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()
