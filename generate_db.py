import sqlite3

# This script creates the actual database file for your GitHub
def create_sample_db():
    conn = sqlite3.connect('market_insight.db')
    cursor = conn.cursor()

    # 1. Create Tables
    cursor.executescript('''
    CREATE TABLE Products (product_id INTEGER PRIMARY KEY, name TEXT, category TEXT);
    CREATE TABLE Internal_Reviews (id INTEGER PRIMARY KEY, p_id INTEGER, comment TEXT, sentiment REAL);
    CREATE TABLE Reddit_Feed (id INTEGER PRIMARY KEY, p_id INTEGER, post TEXT, sentiment REAL, upvotes INTEGER);
    ''')

    # 2. Insert Professional-Looking Sample Data
    products = [(1, 'UltraBook Pro', 'Electronics'), (2, 'Eco-Fit Watch', 'Wearables')]
    cursor.executemany('INSERT INTO Products VALUES (?,?,?)', products)

    # Simulated Website Reviews
    internal = [(1, 1, 'Best laptop for students!', 0.85), (2, 2, 'Battery life is disappointing.', -0.4)]
    cursor.executemany('INSERT INTO Internal_Reviews VALUES (?,?,?,?)', internal)

    # Simulated Reddit Posts
    reddit = [(1, 1, 'UltraBook Pro thermal throttling issues?', -0.3, 150), 
              (2, 2, 'Is the Eco-Fit Watch accurate for heart rate?', 0.1, 45)]
    cursor.executemany('INSERT INTO Reddit_Feed VALUES (?,?,?,?,?)', reddit)

    conn.commit()
    conn.close()
    print("Success! 'market_insight.db' has been created.")

if __name__ == "__main__":
    create_sample_db() 