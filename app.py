import sqlite3
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Simulated Backend Logic
class SentimentEngine:
    def __init__(self, db_path):
        self.db_path = db_path
        self.analyzer = SentimentIntensityAnalyzer()

    def analyze_text(self, text):
        # Returns the compound sentiment score
        return self.analyzer.polarity_scores(text)['compound']

    def get_market_gap(self, product_id):
        # SQL Join to compare Website vs Reddit scores
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        query = """
            SELECT AVG(i.sentiment), AVG(r.sentiment)
            FROM Internal_Reviews i
            JOIN Reddit_Feed r ON i.p_id = r.p_id
            WHERE i.p_id = ?
        """
        return cur.execute(query, (product_id,)).fetchone()
