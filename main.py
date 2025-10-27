import sqlite3
import faker
import random

# Connect (this will create the DB file)
conn = sqlite3.connect("ecommerce.db")
c = conn.cursor()

# Create tables
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    address TEXT,
    created_at TEXT
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    category TEXT,
    price REAL
)
""")

c.execute("""
CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    total REAL,
    created_at TEXT,
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(product_id) REFERENCES products(id)
)
""")

# Faker for generating fake data
fake = faker.Faker()

# Insert users
fake_emails = set()  # Keep track of generated emails
users_to_insert = 50000  # increase number for bigger DB
attempts = 0

while len(fake_emails) < users_to_insert and attempts < users_to_insert * 2:
    email = fake.unique.email()  # Use unique email generator
    if email not in fake_emails:
        fake_emails.add(email)
        c.execute("INSERT INTO users (name, email, address, created_at) VALUES (?, ?, ?, ?)",
                  (fake.name(), email, fake.address(), fake.date_this_decade().isoformat()))
    attempts += 1

# Insert products
categories = ["Electronics", "Books", "Clothing", "Home", "Toys"]
for _ in range(10000):
    c.execute("INSERT INTO products (name, category, price) VALUES (?, ?, ?)",
              (fake.word().capitalize(), random.choice(categories), round(random.uniform(5, 500), 2)))

# Insert orders
for _ in range(200000):  # increase for load testing
    user_id = random.randint(1, 50000)
    product_id = random.randint(1, 10000)
    qty = random.randint(1, 5)
    price = c.execute("SELECT price FROM products WHERE id=?", (product_id,)).fetchone()[0]
    c.execute("INSERT INTO orders (user_id, product_id, quantity, total, created_at) VALUES (?, ?, ?, ?, ?)",
              (user_id, product_id, qty, price * qty, fake.date_time_this_year().isoformat()))

conn.commit()
conn.close()
