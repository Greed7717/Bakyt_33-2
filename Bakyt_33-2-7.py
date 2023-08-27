import sqlite3

def create_database():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title TEXT NOT NULL,
            price REAL DEFAULT 0.0 NOT NULL,
            quantity INTEGER DEFAULT 0 NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

def add_sample_products():
    products = [
        ("Жидкое мыло с запахом ванили", 150.99, 10),
        ("Мыло детское", 75.50, 5),
        ("Шампунь для волос", 250.00, 20),
        ("Зубная паста с мятным вкусом", 80.00, 15),
        # ... и так далее
    ]

    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO products (product_title, price, quantity) VALUES (?, ?, ?)', products)

    conn.commit()
    conn.close()

def update_quantity_by_id(product_id, new_quantity):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET quantity = ? WHERE id = ?', (new_quantity, product_id))

    conn.commit()
    conn.close()

def update_price_by_id(product_id, new_price):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('UPDATE products SET price = ? WHERE id = ?', (new_price, product_id))

    conn.commit()
    conn.close()

def delete_product_by_id(product_id):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM products WHERE id = ?', (product_id,))

    conn.commit()
    conn.close()

def get_all_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products')
    products = cursor.fetchall()

    conn.close()
    return products

def get_affordable_products():
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE price < 100.0 AND quantity > 5')
    products = cursor.fetchall()

    conn.close()
    return products

def search_products_by_title(keyword):
    conn = sqlite3.connect('hw.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM products WHERE product_title LIKE ?', ('%' + keyword + '%',))
    products = cursor.fetchall()

    conn.close()
    return products

create_database()

add_sample_products()

update_quantity_by_id(1, 20)

update_price_by_id(2, 70.0)

delete_product_by_id(3)

all_products = get_all_products()
print("Все товары:")
for product in all_products:
    print(product)

affordable_products = get_affordable_products()
print("\nДоступные товары (дешевле 100 сомов и больше 5 шт.):")
for product in affordable_products:
    print(product)

search_keyword = "мыло"
search_results = search_products_by_title(search_keyword)
print(f"\nРезультаты поиска для '{search_keyword}':")
for product in search_results:
    print(product)
