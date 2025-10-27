# ECommerce SQLite Database Seeder

This Python script generates a **synthetic e-commerce database** using `sqlite3`, `faker`, and `random`.
It creates realistic tables for **users**, **products**, and **orders**, then populates them with thousands of rows of fake data — perfect for **testing**, **analytics**, or **performance benchmarking**.

---

## Overview

The script automatically:

1. Creates a local SQLite database file named `ecommerce.db`
2. Builds three tables:

   - **users** — customer profiles
   - **products** — items for sale
   - **orders** — purchases connecting users and products

3. Populates the tables with large, randomly generated sample data.

---

## Database Schema

### **users**

| Column     | Type    | Description           |
| ---------- | ------- | --------------------- |
| id         | INTEGER | Primary key (auto)    |
| name       | TEXT    | Full name             |
| email      | TEXT    | Unique email address  |
| address    | TEXT    | Physical address      |
| created_at | TEXT    | Account creation date |

### **products**

| Column   | Type    | Description                              |
| -------- | ------- | ---------------------------------------- |
| id       | INTEGER | Primary key (auto)                       |
| name     | TEXT    | Product name                             |
| category | TEXT    | Category (e.g. Electronics, Books, etc.) |
| price    | REAL    | Product price                            |

### **orders**

| Column     | Type    | Description               |
| ---------- | ------- | ------------------------- |
| id         | INTEGER | Primary key (auto)        |
| user_id    | INTEGER | References `users(id)`    |
| product_id | INTEGER | References `products(id)` |
| quantity   | INTEGER | Number of items ordered   |
| total      | REAL    | Total order amount        |
| created_at | TEXT    | Order timestamp           |

---

## Setup & Usage

### **1. Install dependencies**

```bash
pip install faker
```

### **2. Run the script**

```bash
python seed_ecommerce_db.py
```

This will create (or overwrite) an SQLite database file named **`ecommerce.db`** in the current directory.

---

## Default Data Volume

| Table    | Rows Generated | Notes                                               |
| -------- | -------------- | --------------------------------------------------- |
| users    | 50,000         | Unique names, emails, and addresses                 |
| products | 10,000         | Random categories and prices                        |
| orders   | 200,000        | Randomized relationships between users and products |

> 💡 You can increase or decrease these numbers by editing the variables:
>
> ```python
> users_to_insert = 50000
> for _ in range(10000):  # products
> for _ in range(200000):  # orders
> ```

---

## Notes

- Uses `faker` for realistic user and order data.
- Ensures unique emails for all users.
- Enforces foreign key relationships between users and orders.
- Ideal for load testing APIs, analytics, or dashboard mockups.

---

## Cleanup

To reset the database:

```bash
rm ecommerce.db
```

Then rerun the script.
