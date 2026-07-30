-- Main Product Catalog
CREATE TABLE Products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_name TEXT NOT NULL,
    category TEXT
);

-- Internal Website Reviews (HTML Form Data)
CREATE TABLE Internal_Reviews (
    review_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    user_name TEXT,
    review_text TEXT,
    sentiment_score REAL,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);

-- External Reddit Data (API Data)
CREATE TABLE Reddit_Feed (
    reddit_id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_id INTEGER,
    subreddit TEXT,
    post_title TEXT,
    upvote_count INTEGER,
    sentiment_score REAL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
);
